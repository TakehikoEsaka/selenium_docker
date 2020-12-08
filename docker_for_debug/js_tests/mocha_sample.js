// yarn addで入れたpackageを利用する時はrequireを使う
var assert = require('assert');

// describeはmocha専用のfunctionで引数にstring(説明文)とfunctionを引数に取れる
describe('indexOf()', function() {
    // it関数の第一引数にテストしたいstringを記載。第二引数にテスト内容を書いた関数を指定
    it('should return -1 when the value is not present', function() {
        assert.equal([1,2,3].indexOf(4), -1);
    });
});