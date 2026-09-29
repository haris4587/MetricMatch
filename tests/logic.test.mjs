import {test} from 'node:test';
import {strict as assert} from 'node:assert';
import {numericInput, parseClaim, parseChallenge, compare} from '../src/logic.ts';

test('malformed contract state is rejected before rendering',()=>{
  assert.throws(()=>parseClaim('{"status":"OPEN"}'),/Invalid contract response/);
  assert.throws(()=>parseClaim('not json'),SyntaxError);
  assert.equal(parseChallenge(''),null);
});

test('whole-number bounds match the contract u32 input',()=>{
  for(const bad of ['0','-1','1.5','4294967296','Infinity','abc'])
    assert.throws(()=>numericInput(bad),/positive whole number/);
  assert.equal(numericInput('4294967295'),4294967295);
});

test('the two score directions produce opposite refutation outcomes',()=>{
  const base={claimed_value:40,lower_is_better:true};
  const observed={observed_value:48};
  assert.equal(compare(base,observed),true);
  assert.equal(compare({...base,lower_is_better:false},observed),false);
});
