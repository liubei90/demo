// import { frame } from '../common';
import * as frame from '../common/frame.js';
var btn1 = document.querySelector('#btn1');

btn1.addEventListener('click', function(env) {
  frame.registModule({
    page: 'page1'
  });

  import('./m1').then(function(m) {
    console.log(m)
    var add = m.default;
    console.log('2 + 3 =', add(2, 3));
    console.log(m.testStr);
  });
});
