import {createClient} from 'genlayer-js';
import {studionet} from 'genlayer-js/chains';
import {TransactionHashVariant, TransactionStatus} from 'genlayer-js/types';
import type {CalldataEncodable} from 'genlayer-js/types';

export function readClient() { return createClient({chain:studionet}); }
export async function read(address:string, functionName:string, args:CalldataEncodable[] = []) {
  return readClient().readContract({address:address as `0x${string}`, functionName, args, transactionHashVariant:TransactionHashVariant.LATEST_FINAL});
}
export async function signedWrite(address:string, functionName:string, args:CalldataEncodable[]) {
  const provider = (window as Window & {ethereum?:unknown}).ethereum;
  if (!provider) throw new Error('A compatible browser wallet is needed for writes. Studio’s built-in wallet can transact in Studio.');
  const accounts = await (provider as {request:(x:{method:string})=>Promise<string[]>}).request({method:'eth_requestAccounts'});
  if (!accounts?.[0]) throw new Error('No wallet account selected');
  const client = createClient({chain:studionet, account:accounts[0] as `0x${string}`, provider:provider as never});
  await client.connect('studionet');
  const hash = await client.writeContract({address:address as `0x${string}`, functionName, args, value:0n});
  const receipt = await client.waitForTransactionReceipt({hash, status:TransactionStatus.FINALIZED});
  if (receipt.txExecutionResultName !== 'FINISHED_WITH_RETURN') throw new Error(`Transaction ${hash} failed: ${receipt.statusName} / ${receipt.txExecutionResultName}`);
  return hash;
}
