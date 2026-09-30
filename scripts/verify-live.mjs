import {execFileSync} from 'node:child_process';
import {writeFileSync} from 'node:fs';
import {createClient} from 'genlayer-js';
import {studionet} from 'genlayer-js/chains';
import {TransactionHashVariant} from 'genlayer-js/types';
// Optional curl transport for environments that route HTTPS through a proxy.
if (process.env.METRICMATCH_CURL_TRANSPORT === '1') {
  globalThis.fetch = async (url, options) => {
    if (String(url) !== 'https://studio.genlayer.com/api') throw new Error('Unexpected endpoint');
    const body = execFileSync('curl', ['--fail-with-body','-sS',String(url),'-H','Content-Type: application/json','--data-binary','@-'], {input:options.body,encoding:'utf8'});
    return new Response(body,{status:200,headers:{'Content-Type':'application/json'}});
  };
}
const address = '0x3F251a2330c21312093cf76e8AC10274b40D155D';
const client = createClient({chain:studionet});
const results = {network:'studionet',address,checked_at:new Date().toISOString(),state:'LATEST_FINAL',claims:[],accounting:null};
for (const id of [0,1]) results.claims.push(JSON.parse(await client.readContract({address,functionName:'get_claim',args:[id],transactionHashVariant:TransactionHashVariant.LATEST_FINAL})));
results.accounting=JSON.parse(await client.readContract({address,functionName:'get_accounting',args:[],transactionHashVariant:TransactionHashVariant.LATEST_FINAL}));
if (results.claims[0].status !== 'REFUTED' || results.claims[1].status !== 'INCONCLUSIVE') throw new Error('Unexpected outcomes');
for (const key of ['balance_wei','locked_wei','credit_wei']) if(results.accounting[key] !== '0') throw new Error(`Outstanding ${key}`);
if(results.accounting.withdrawn_wei !== '4000000000000000000') throw new Error('Withdrawal total mismatch');
writeFileSync('evidence/finalized-state.json',JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(results,null,2));
