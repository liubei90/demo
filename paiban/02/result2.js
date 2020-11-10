var student_depart = {
  "张超": "心病科",
  "王棣丞": "心病科",
  "邱月清": "心病科",
  "潘海涛": "心病科",
  "刘建申": "心病科",
  "李治兵": "心病科",
  "李习婉": "心病科",
  "郑璐璐": "肝胆脾胃病科",
  "赵永华": "肝胆脾胃病科",
  "张鑫丽": "肝胆脾胃病科",
  "张璐鹏": "肝胆脾胃病科",
  "张开波": "肝胆脾胃病科",
  "王露": "肝胆脾胃病科",
  "莫万灵": "肝胆脾胃病科",
  "娄方敏": "肝胆脾胃病科",
  "李英宵": "肝胆脾胃病科",
  "李倩倩": "肝胆脾胃病科",
  "贺群慧": "心病科",
  "樊亚芳": "肝胆脾胃病科",
  "胡颖": "血液科",
  "黄爱娟": "内分泌",
  "崔艳粉": "脑病科",
  "张亚乐": "内分泌",
  "任宗浩": "内分泌",
  "吉兰洁": "内分泌",
  "张迪": "心病科",
  "邢玉凤": "肾病",
  "张创业": "脑病科",
  "任闪闪": "脑病科",
  "马瑞红": "脑病科",
  "李锋森": "老年病",
  "侯露阳": "脑病科",
  "范莹莹": "脑病科",
  "代云": "脑病科",
  "成家宏": "老年病",
  "袁帆": "肿瘤",
  "袁成凤": "肿瘤",
  "叶子": "肿瘤",
  "王若凡": "肿瘤",
  "王红艳": "肿瘤",
  "苏珊珊": "肿瘤",
  "邵帅": "肿瘤",
  "任娟": "肿瘤",
  "李颖": "脑病科",
  "李登科": "肿瘤",
  "康研": "肿瘤",
  "介睿峥": "肿瘤",
  "陈梦利": "肿瘤",
  "侯学文": "肺病科",
  "李方方": "脑病科",
  "孟六阳": "脑病科",
  "张静晓": "肝胆脾胃病科",
  "朱丹娜": "肺病科",
  "段启": "肿瘤"
}


function fix_result() {
  var keys = Object.keys(min_student);
  for (var i = 0; i < keys.length; i++) {
    var cur_stu = min_student[keys[i]];
    var last = cur_stu['last'].filter(function(item) { return item !== place_holder_department });
    var last_i = 0;
    var result = cur_stu['result'];

    for (var j = 0; j < result.length; j++) {
      if (result[j] === place_holder_department && last_i < last.length) {
        result[j] = last[last_i];
        last_i++;
      }
    }
  }
}

fix_result()

var select_depart = ['老年病', '肿瘤', '血液科'];


var keys = Object.keys(min_student);
for (var i = 0; i < keys.length; i++) {
  var stu = min_student[keys[i]];
  var dep = student_depart[keys[i]];
  var result = stu['result'];
  stu['own_depart'] = dep;

  // 去除自身部门
  for (var j = 2; j < result.length; j++) {
    if (dep === result[j]) {
      if (dep !== '内分泌') {
        result[j] = '内分泌';
      } else {
        result[j] = '肾病';
      }
      
    };
  }

  // 随机选转部门
  var rmi = 0;
  for (var j = 0; j < result.length; j++) {
    if (result[j] === '内分泌' || result[j] === '肾病') {
      if (!result[result[j]]) {
        result[result[j]] = true;
      } else {
        result[j] = select_depart[Math.floor(Math.random()*select_depart.length)];
      }
    };
  }
}
