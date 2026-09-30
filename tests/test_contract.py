"""Execute release contract methods with a strict mocked GenVM boundary.
These tests cover deterministic logic; the recorded live run verifies consensus/transfers.
"""
import importlib.util
import json
import pathlib
import sys
import types
import unittest

class UserError(Exception): pass
class Decorator:
    def __call__(self, fn): return fn
    payable = property(lambda self: self)
class TreeMap(dict):
    @classmethod
    def __class_getitem__(cls, args): return cls
class Address(str):
    def __new__(cls, s): return str.__new__(cls, s.lower())
class Return:
    def __init__(self, value): self.calldata = value
class Contract: pass
class Recipient:
    def __init__(self, addr): self.addr=addr
    def emit_transfer(self, value):
        env.transfers.append((self.addr,value))
        env.contract.balance -= value

def consensus(assess, validate):
    result = assess()
    if not validate(Return(result)): raise UserError('Validator disagreement')
    return result

env=types.SimpleNamespace()
gl=types.SimpleNamespace(Contract=Contract, public=types.SimpleNamespace(write=Decorator(),view=Decorator()),
    evm=types.SimpleNamespace(contract_interface=lambda _: Recipient),
    vm=types.SimpleNamespace(UserError=UserError,Return=Return,run_nondet_unsafe=consensus),
    message=types.SimpleNamespace(sender_address=Address('0x'+'1'*40),value=0),
    nondet=types.SimpleNamespace(web=types.SimpleNamespace(),exec_prompt=lambda _: 'COMPARABLE'))
module=types.ModuleType('genlayer')
for k,v in dict(gl=gl,u32=int,u256=int,TreeMap=TreeMap,Address=Address).items(): setattr(module,k,v)
sys.modules['genlayer']=module
path=pathlib.Path(__file__).resolve().parents[1]/'contracts/metric_match.py'
spec=importlib.util.spec_from_file_location('release_contract',path)
release=importlib.util.module_from_spec(spec); spec.loader.exec_module(release)

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.c=release.MetricMatch(); self.c.claims=TreeMap(); self.c.challenges=TreeMap(); self.c.credits=TreeMap()
        self.c.balance=0; self.now=1000000; self.c._now=lambda: self.now
        env.contract=self.c; env.transfers=[]
        gl.nondet.web.get=lambda _: types.SimpleNamespace(status=200,body=b'Original 40 seconds, observed 48 seconds, identical workload')
        gl.nondet.exec_prompt=lambda _: 'COMPARABLE'
        self.owner=Address('0x'+'1'*40); self.challenger=Address('0x'+'2'*40)
        self.sender(self.owner)
    def sender(self, addr, value=0): gl.message.sender_address=addr; gl.message.value=value
    def create(self, stake=10, direction=True):
        self.sender(self.owner,stake)
        self.c.create_claim('Build time claim','Example v1','Build time',40,'seconds',direction,'Identical hardware and workload','https://example.com/original',1)
        self.c.balance+=stake
    def challenge(self, stake=10, value=48):
        self.sender(self.challenger,stake); self.c.challenge(0,'https://example.com/challenge',value); self.c.balance+=stake
    def claim(self): return json.loads(self.c.get_claim(0))
    def check_accounting(self):
        a=json.loads(self.c.get_accounting())
        self.assertEqual(int(a['deposited_wei']),int(a['locked_wei'])+int(a['credit_wei'])+int(a['withdrawn_wei']))
    def test_lower_refuted_withdraws_pool_once(self):
        self.create(); self.challenge(); self.c.evaluate(0)
        self.assertEqual(self.claim()['status'],'REFUTED'); self.assertEqual(self.c.get_credit(self.challenger),'20')
        self.c.withdraw(); self.assertEqual(env.transfers,[(self.challenger,20)]); self.assertEqual(self.c.balance,0)
        with self.assertRaises(UserError): self.c.withdraw()
        self.check_accounting()
    def test_higher_is_better_upheld(self):
        self.create(direction=False); self.challenge(); self.c.evaluate(0)
        self.assertEqual(self.c.get_credit(self.owner),'20'); self.assertEqual(self.claim()['status'],'UPHELD'); self.check_accounting()
    def test_equal_result_upholds(self):
        self.create(); self.challenge(value=40); self.c.evaluate(0); self.assertEqual(self.claim()['status'],'UPHELD')
    def test_not_comparable_awards_owner(self):
        self.create(); self.challenge(); gl.nondet.exec_prompt=lambda _: 'NOT_COMPARABLE'; self.c.evaluate(0)
        self.assertEqual(self.c.get_credit(self.owner),'20')
    def test_inconclusive_three_attempts_refund_both(self):
        self.create(); self.challenge(); gl.nondet.exec_prompt=lambda _: 'INCONCLUSIVE'
        for _ in range(3): self.c.evaluate(0)
        self.assertEqual(self.claim()['status'],'INCONCLUSIVE'); self.assertEqual(self.c.get_credit(self.owner),'10'); self.assertEqual(self.c.get_credit(self.challenger),'10')
        self.assertEqual(len(self.claim()['history']),3); self.check_accounting()
    def test_non_200_does_not_call_llm(self):
        self.create(); self.challenge(); gl.nondet.web.get=lambda _: types.SimpleNamespace(status=404,body=b'40 48')
        gl.nondet.exec_prompt=lambda _: self.fail('HTTP error reached LLM'); self.c.evaluate(0); self.assertEqual(self.claim()['verdict'],'INCONCLUSIVE')
    def test_empty_body_inconclusive(self):
        self.create(); self.challenge(); gl.nondet.web.get=lambda _: types.SimpleNamespace(status=200,body=b''); self.c.evaluate(0); self.assertEqual(self.claim()['verdict'],'INCONCLUSIVE')
    def test_wrong_api_property_fails(self):
        self.create(); self.challenge(); gl.nondet.web.get=lambda _: types.SimpleNamespace(status_code=200,body=b'40 48')
        with self.assertRaises(AttributeError): self.c.evaluate(0)
    def test_validator_disagreement_leaves_unsettled(self):
        self.create(); self.challenge(); answers=iter(['COMPARABLE','NOT_COMPARABLE']); gl.nondet.exec_prompt=lambda _:next(answers)
        with self.assertRaisesRegex(UserError,'disagreement'): self.c.evaluate(0)
        self.assertEqual(self.claim()['attempts'],0); self.assertFalse(self.claim()['settled'])
    def test_exact_stake_match_required(self):
        self.create(); self.sender(self.challenger,9)
        with self.assertRaises(UserError): self.c.challenge(0,'https://example.com/challenge',48)
        self.assertEqual(self.claim()['status'],'OPEN')
    def test_self_challenge_rejected(self):
        self.create(); self.sender(self.owner,10)
        with self.assertRaises(UserError): self.c.challenge(0,'https://example.com/challenge',48)
    def test_duplicate_challenge_rejected(self):
        self.create(); self.challenge()
        with self.assertRaises(UserError): self.c.challenge(0,'https://example.com/other',49)
    def test_unchallenged_deadline_refund(self):
        self.create(); self.now=self.claim()['deadline']; self.c.close_unchallenged(0)
        self.assertEqual(self.c.get_credit(self.owner),'10'); self.assertEqual(self.claim()['status'],'UNCHALLENGED'); self.check_accounting()
    def test_resolution_timeout_refunds(self):
        self.create(); self.challenge(); self.now=self.claim()['resolution_deadline']; self.c.expire_unresolved(0)
        self.assertEqual(self.c.get_credit(self.owner),'10'); self.assertEqual(self.c.get_credit(self.challenger),'10'); self.check_accounting()
    def test_no_early_timeout(self):
        self.create(); self.challenge()
        with self.assertRaises(UserError): self.c.expire_unresolved(0)
    def test_no_second_settlement(self):
        self.create(); self.challenge(); self.c.evaluate(0)
        with self.assertRaises(UserError): self.c.evaluate(0)
        with self.assertRaises(UserError): self.c.expire_unresolved(0)
        self.check_accounting()
    def test_stake_cap_and_https(self):
        with self.assertRaises(UserError): self.create(1001*10**18)
        with self.assertRaises(UserError): self.c._url('http://example.com')
    def test_zero_stakes_supported(self):
        self.create(0); self.challenge(0); self.c.evaluate(0); self.assertEqual(self.claim()['status'],'REFUTED'); self.check_accounting()

if __name__ == '__main__': unittest.main()
