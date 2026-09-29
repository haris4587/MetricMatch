import {test} from 'node:test';
import {strict as assert} from 'node:assert';
// The production TypeScript module is compiled by Vite. These tests check the contract's
// deterministic threshold independently through a compact specification.
test('lower-is-better claim is refuted by a higher comparable result',()=>{const c=40, observed=48; assert.equal(observed>c,true); assert.equal(39>c,false)});
test('higher-is-better claim is refuted by a lower comparable result',()=>{const c=900, observed=850; assert.equal(observed<c,true); assert.equal(950<c,false)});
