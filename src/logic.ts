export type Claim = {id:number; owner:string; title:string; product:string; metric:string; claimed_value:number; unit:string; lower_is_better:boolean; conditions:string; evidence_url:string; deadline:number; status:string; verdict:string; attempts:number; stake_wei:string; resolution_deadline:number; settled:boolean; owner_credit_wei:string; challenger_credit_wei:string};
export type Challenge = {challenger:string; evidence_url:string; observed_value:number; submitted_at:number};
export function parseClaim(raw:unknown):Claim { const value = typeof raw === 'string' ? JSON.parse(raw) : raw; if (!value || typeof value.id !== 'number' || typeof value.status !== 'string') throw new Error('Invalid contract response'); return value as Claim; }
export function parseChallenge(raw:unknown):Challenge|null { if (!raw) return null; const value = typeof raw === 'string' ? JSON.parse(raw) : raw; return value && value.challenger ? value as Challenge : null; }
export function numericInput(value:string):number { const n = Number(value); if (!Number.isSafeInteger(n) || n <= 0 || n > 4294967295) throw new Error('Enter a positive whole number up to 4,294,967,295'); return n; }
export function compare(claim:Claim, challenge:Challenge):boolean { return claim.lower_is_better ? challenge.observed_value > claim.claimed_value : challenge.observed_value < claim.claimed_value; }

export function stakeInput(value:string):bigint {
  if (!/^\d+(\.\d{1,18})?$/.test(value)) throw new Error('Enter GEN with at most 18 decimal places');
  const [whole,fraction=''] = value.split('.');
  const wei=BigInt(whole)*10n**18n+BigInt(fraction.padEnd(18,'0'));
  if(wei>1000n*10n**18n) throw new Error('Stake is limited to 1000 GEN');
  return wei;
}
export function formatGen(value:string):string {
 const n=BigInt(value),fraction=(n%10n**18n).toString().padStart(18,'0').replace(/0+$/,'');
 return (n/10n**18n).toString()+(fraction?'.'+fraction:'');
}
