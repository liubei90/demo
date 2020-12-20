// import { frame } from '../common';
import * as frame from '../common/frame.js';
var btn1 = document.querySelector('#btn1');

btn1.addEventListener('click', function(env) {
  frame.registModule({
    page: 'page1'
  });

});
