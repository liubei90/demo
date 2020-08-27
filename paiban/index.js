var must_transfer_department = ['心病科', 'ICU', '肝胆脾胃病科', '肺病科', '脑病科', '肾病', '内分泌', '急诊'];
var select_transfer_department = ['老年病'];
// var must_transfer_department = ['急诊', '心病科', 'ICU', '肝胆脾胃病科', '肺病科', '脑病科'];
// var select_transfer_department = ['肾病', '内分泌', '老年病', '肿瘤', '血液科'];

var must_transfer_section = ['急诊', '心病一区', '心病二区', 'ICU', '肝胆脾胃一区', '肝胆脾胃二区', '肝胆脾胃三区', '肺病科', '脑病一区', '脑病二区', '脑病三区', '肾病', '内分泌'];

var two_mouths_depart = ['急诊', '心病科'];
var two_mouths_section = ['急诊', '心病一区', '心病二区'];
var must_transfer_department_mouths = {
  '急诊': 2, 
  '心病科': 2, 
  'ICU': 1, 
  '肝胆脾胃病科': 1, 
  '肺病科': 1, 
  '脑病科': 1,
}

var department_sections = {
  '心病科': ['心病一区', '心病二区'],
  '脑病科': ['脑病一区', '脑病二区', '脑病三区'],
  '肝胆脾胃病科': ['肝胆脾胃一区', '肝胆脾胃二区', '肝胆脾胃三区'],
  '肺病科': ['肺病科'],
  '急诊': ['急诊'],
  'ICU': ['ICU'],
  '肾病': ['肾病'],
  '血液科': ['血液'],
  '内分泌': ['内分泌'],
  '肿瘤': ['肿瘤一区', '肿瘤二区', '肿瘤三区'],
  '老年病': ['老年病'],
}

function get_random_section_in_depart(depart) {
  var sections = department_sections[depart];
  var index = Math.floor(Math.random() * sections.length);

  return sections[index];
}

var department_sections_keys = Object.keys(department_sections);

var transfer_section_arr = [];
var transfer_section_info = {};

(function() {
  for (var i = 0; i < department_sections_keys.length; i++) {
    var depart = department_sections_keys[i];
    var sectionlist = department_sections[depart];

    for (var j = 0; j < sectionlist.length; j++) {
      var section = sectionlist[j];
      transfer_section_arr.push(section);
      transfer_section_info[section] = {
        is_must: false,
        is_select: false,
        section: section,
        depart: depart,
        must_mouth: must_transfer_department_mouths[depart],
      }
    }
  }
})();

(function() {
  var sections = null;
  // 必转
  for (var i = 0; i < must_transfer_department.length; i++) {
    sections = department_sections[must_transfer_department[i]];

    for (var j = 0; j < sections.length; j++) {
      transfer_section_info[sections[j]].is_must = true;
    }
  }

  // 选转
  for (var i = 0; i < select_transfer_department.length; i++) {
    sections = department_sections[select_transfer_department[i]];

    for (var j = 0; j < sections.length; j++) {
      transfer_section_info[sections[j]].is_select = true;
    }
  }
})();

// console.dir(transfer_section_arr);
// console.dir(transfer_section_info, { depth: 10 });

function is_must_section(section) {
  return transfer_section_info[section].is_must;
}

function is_select_section(section) {
  return transfer_section_info[section].is_select;
}

function get_must_mouth(section) {
  return transfer_section_info[section].must_mouth;
}

function get_depart_name(section) {
  return transfer_section_info[section].depart;
}

function is_must_department(depart) {
  return must_transfer_department.indexOf(depart) > -1;
}

function is_select_department(depart) {
  return select_transfer_department.indexOf(depart) > -1;
}


var students = ["成家宏","邢玉凤","马瑞红","侯学文","朱丹娜","崔艳粉","张创业","孟六阳","张迪","潘海涛","赵永华","张超","刘建申","莫万灵","胡颖","贺群慧","王露","段启","代云","王棣丞","任闪闪","李锋森","范莹莹","李登科","介睿峥","苏珊珊","邱月清","李英宵","樊亚芳","李治兵","李习婉","王若凡","李倩倩","任娟","张鑫丽","袁成凤","郑璐璐","娄方敏","叶子","王红艳","张亚乐","黄爱娟","任宗浩","吉兰洁","李颖","张静晓","袁帆","侯露阳","张璐鹏","张开波","康研","李方方","邵帅","陈梦利"];

var students_wish = {
  "张超": ["内分泌","肾病","血液科","肿瘤"],
  "王棣丞": ["内分泌","肾病","血液科","肿瘤","肝二"],
  "邱月清": ["肾病","内分泌","血液科","肿瘤"],
  "潘海涛": ["内分泌","肾病","血液科","肿瘤"],
  "刘建申": ["内分泌","肾病","血液科","肿瘤"],
  "李治兵": ["内分泌","肾病","血液科","肿瘤"],
  "李习婉": ["内分泌","老年病","肾病","血液科"],
  "郑璐璐": ["内分泌","老年病","肾病","血液科"],
  "赵永华": ["内分泌","老年病","肾病",""],
  "张鑫丽": ["老年病","内分泌","肿瘤","肾病"],
  "张璐鹏": ["内分泌","肾病"],
  "张开波": ["内分泌","肾病"],
  "王露": ["老年病","内分泌","血液科","肾病"],
  "莫万灵": ["内分泌","内分泌","老年病"],
  "娄方敏": ["内分泌","肾病","老年病","肝一"],
  "李英宵": ["内分泌","肾病","老年病"],
  "李倩倩": ["内分泌","肾病","肿瘤","老年病,ICU"],
  "贺群慧": ["肿瘤","老年病","肾病","内分泌"],
  "樊亚芳": ["肿瘤","老年病","肾病","内分泌"],
  "胡颖": ["内分泌","肾病"],
  "黄爱娟": ["内分泌","内分泌"],
  "崔艳粉": ["内分泌","肿瘤","肾病"],
  "张亚乐": ["内分泌","内分泌"],
  "任宗浩": ["内分泌"],
  "吉兰洁": ["内分泌","内分泌"],
  "张迪": ["内分泌","内分泌","肾病","老年病",""],
  "邢玉凤": ["肿瘤","老年病"],
  "张创业": ["内分泌","肾病","肿瘤"],
  "任闪闪": ["肾病","内分泌","肿瘤"],
  "马瑞红": ["内分泌","肾病","老年病","血液科"],
  "李锋森": ["老年病","内分泌"],
  "侯露阳": ["老年病","肾病","肿瘤"],
  "范莹莹": ["内分泌","肿瘤","肾病","老年病"],
  "代云": ["老年病","内分泌","肾病"],
  "成家宏": ["老年病","肾病","内分泌","血液科"],
  "袁帆": ["老年病","血液科","ICU","内分泌"],
  "袁成凤": ["老年病","肾病","内分泌","血液科"],
  "叶子": ["老年病","内分泌","血液科","ICU"],
  "王若凡": ["老年病","内分泌","血液科","ICU"],
  "王红艳": ["老年病","内分泌","ICU","血液科"],
  "苏珊珊": ["老年病","肾病","内分泌","ICU"],
  "邵帅": ["肝胆脾胃病科","内分泌","肾病","肺病科"],
  "任娟": ["内分泌","肾病"],
  "李颖": ["内分泌","肿瘤","肾病"],
  "李登科": ["内分泌","老年病","血液科","肾病"],
  "康研": ["内分泌","肾病","血液科","ICU"],
  "介睿峥": ["内分泌","肾病","老年病","血液科"],
  "陈梦利": ["肝胆脾胃病科","内分泌","肾病","肺病科"],
  "侯学文": ["内分泌","肾病","肿瘤","血液科"],
  "李方方": ["内分泌","ICU","肿瘤","肾病"],
  "孟六阳": ["肾病","内分泌","肿瘤"],
  "张静晓": ["肿瘤","内分泌","肾病","ICU","老年病"],
  "朱丹娜": ["内分泌","血液科","肿瘤"],
  "段启": ["老年病","肾病","内分泌"],
}

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

var results_8 = {
  "成家宏": ["心病一区"],
  "邢玉凤": ["心病一区"],
  "马瑞红": ["心病一区"],
  "侯学文": ["心病一区"],
  "朱丹娜": ["心病二区"],
  "崔艳粉": ["心病二区"],
  "张创业": ["心病二区"],
  "孟六阳": ["心病二区"],
  "张迪": ["脑病一区"],
  "潘海涛": ["脑病一区"],
  "赵永华": ["脑病一区"],
  "张超": ["脑病二区"],
  "刘建申": ["脑病二区"],
  "莫万灵": ["脑病二区"],
  "胡颖": ["脑病三区"],
  "贺群慧": ["脑病三区"],
  "王露": ["脑病三区"],
  "段启": ["肝胆脾胃一区"],
  "代云": ["肝胆脾胃一区"],
  "王棣丞": ["肝胆脾胃二区"],
  "任闪闪": ["肝胆脾胃二区"],
  "李锋森": ["肝胆脾胃三区"],
  "范莹莹": ["肝胆脾胃三区"],
  "李登科": ["肝胆脾胃三区"],
  "介睿峥": ["肺病科"],
  "苏珊珊": ["肺病科"],
  "邱月清": ["肺病科"],
  "李英宵": ["肺病科"],
  "樊亚芳": ["肺病科"],
  "李治兵": ["急诊"],
  "李习婉": ["急诊"],
  "王若凡": ["急诊"],
  "李倩倩": ["急诊"],
  "任娟": ["急诊"],
  "张鑫丽": ["急诊"],
  "袁成凤": ["急诊"],
  "郑璐璐": ["ICU"],
  "娄方敏": ["ICU"],
  "叶子": ["ICU"],
  "王红艳": ["ICU"],
  "张亚乐": ["肾病"],
  "黄爱娟": ["肾病"],
  "任宗浩": ["肾病"],
  "吉兰洁": ["肾病"],
  "李颖": ["血液"],
  "张静晓": ["血液"],
  "袁帆": ["内分泌"],
  "侯露阳": ["内分泌"],
  "张璐鹏": ["肿瘤三区"],
  "张开波": ["肿瘤三区"],
  "康研": ["老年病"],
  "李方方": ["老年病"],
  "邵帅": ["老年病"],
  "陈梦利": ["老年病"],
}


function get_8_section(student) {
  return results_8[student][0];
}


var students_info = {};

(function() {
  for (var i = 0; i < students.length; i++) {
    students_info[students[i]] = {
      name: students[i],
      // sections: [...results_8[students[i]]],
      sections: [],
      wishs: students_wish[students[i]],
    }
  }
})();

function is_student_selected_section(student, section) {
  var sections = student.sections;

  return sections.indexOf(section) > -1;
}

function is_student_selected_section_in_pre_mouth(student, section) {
  var sections = student.sections;

  return sections[sections.length - 1] === section;
}

function get_select_section_count(student, section) {
  var sections = student.sections;

  var selected = sections.filter(function(item) { return item === section; });
  return selected.length;
}

function get_sections_count(student) {
  return student.sections.length;
}

function get_student_must_count(student) {
  var sections = student.sections;
  var musts = sections.filter(function(item) { return is_must_section(item); });

  return musts.length;
}

function get_student_select_count(student) {
  var sections = student.sections;
  var selects = sections.filter(function(item) { return is_select_section(item); });

  return selects.length;
}

function is_student_pre_selected_two_mouth(student) {
  var sections = student.sections;
  var pre = sections[sections.length - 1];

  return get_must_mouth(pre) === 2;
}

function is_student_pre_pre_selected_two_mouth(student) {
  var sections = student.sections;

  if (sections.length < 2) {
    return false
  }

  var pre_pre = sections[sections.length - 2];
  return get_must_mouth(pre_pre) === 2;
}


var mouth_count = 10;
// var mouth_count = 2;
// 科室已排人员
var section_students = [];
var depart_students = [];

function new_section_students() {
  var res = {};
  for (var i = 0; i < transfer_section_arr.length; i++) {
    res[transfer_section_arr[i]] = [];
  }

  return res;
}

function new_depart_students() {
  var res = {};

  for (var i = 0; i < department_sections_keys.length; i++) {
    res[department_sections_keys[i]] = [];
  }

  return res;
}

(function() {
  for (var i = 0; i < mouth_count; i++) {
    section_students[i] = new_section_students();
  }

  for (var i = 0; i < mouth_count; i++) {
    depart_students[i] = new_depart_students();
  }

  // var first_section_students = section_students[0];
  // var first_depart_students = depart_students[0];
  // var keys = Object.keys(results_8);

  // for (var i = 0; i < keys.length; i++) {
  //   var student = keys[i];
  //   var section = results_8[student][0];
  //   var depart = get_depart_name(section);

  //   first_section_students[section].push(student);
  //   first_depart_students[depart].push(student);
  // }

})();


// 一次排9个月的班
var togeter_students = [
  ['任宗浩', '张开波', '李治兵','张璐鹏'],
  ['陈梦利', '邵帅'],
  ['康研','李方方']
];

var togeter_students_index = {
  '任宗浩': 0, 
  '张开波': 0, 
  '李治兵': 0,
  '张璐鹏': 0,
  '陈梦利': 1, 
  '邵帅': 1,
  '康研': 2,
  '李方方': 2,
}

var togeter_students_tmp = [];

// 7个月
var depart_tmp = [null];

function new_depart_count() {
  var res = {};

  for(var i = 0; i < must_transfer_department.length; i++) {
    res[must_transfer_department[i]] = 0;
  }

  return res;
}

(function() {
  for (var i = 1; i < 8; i++) {
    depart_tmp[i] = new_depart_count();
  }
})();

var depart_score = {
  '急诊': 7, 
  '心病科': 3, 
  'ICU': 6, 
  '肝胆脾胃病科': 2, 
  '肺病科': 6, 
  '脑病科': 2, 
  '肾病': 3, 
  '内分泌': 1
}

function add_student_in_depart(mouth, depart) {
  var mouth_depart = depart_tmp[mouth];
  mouth_depart[depart] += depart_score[depart];
}

function get_less_student_count_depart(mouth, exclude_depart, si) {
  var mouth_depart = depart_tmp[mouth];
  var departs = Object.keys(mouth_depart);
  // 随机
  // departs.sort(() => {return Math.random() > 0.5 ? 1 : -1});
  var min_depart_count = 1000;
  var min_depart = null;

  for(var i = 0; i < departs.length; i++) {
    var index = (si + i + 1) % departs.length;
    var d = departs[index];
    if (exclude_depart.indexOf(d) > -1) {
      continue;
    }

    if (mouth_depart[d] < min_depart_count) {
      min_depart_count = mouth_depart[d];
      min_depart = d;
    }
  }

  return min_depart;
}


function random_sort_must_depart(student, si) {
  var name = student.name;
  var is_torget = false;

  // // 是否在一起得学员
  // var torget_index = togeter_students_index[name];

  // if (torget_index !== undefined) {
  //   is_torget = true;
  // }

  // var torget_tmp = togeter_students_tmp[torget_index];

  // if (torget_tmp) {
  //   return torget_tmp.slice();
  // }

  // var departs = must_transfer_department.slice();

  // // 排除学生所在科室
  // var ex_depart = student_depart[name];
  // var ex_index = departs.indexOf(ex_depart);
  // var other_departs = ['老年病', '肿瘤', '血液科'].filter(function(item) { return item !== ex_depart });

  // if (ex_index > -1) {
  //   departs.splice(ex_index, 1, other_departs[0]);
  // }

  // departs.sort(function(a, b) { return Math.random() > 0.5 ? 1 : -1 });

  // // 将8月分的排在第一位
  // var section_8 = get_8_section(name);
  // var depart_8 = get_depart_name(section_8);
  // var index_8 = departs.indexOf(depart_8);
  // // 非必转科室，默认为 内分泌或肾病
  // if (index_8 < 0) {
  //   index_8 = departs.indexOf('内分泌');
  //   if (index_8 < 0) {
  //     index_8 = departs.indexOf('肾病');
  //   }
  // }
  // var tmp = departs[index_8];
  // departs[index_8] = departs[0];
  // departs[0] = tmp;

  // if (is_torget) {
  //   togeter_students_tmp[torget_index] = departs.slice();
  // }

  // 均匀科室学生数量
  // for (var i = 1; i < random_sections.length; i++) {
  //   var cur_section = random_sections[i];

  //   if (is_section_student_count_over(cur_section, i)) {
  //     var new_section = get_less_student_count_section(i);
  //     var ns_index = random_sections.indexOf(new_section);

  //     if (ns_index > -1) {
  //       var tmp = random_sections[ns_index];

  //       random_sections[ns_index] = random_sections[i];
  //       random_sections[i] = tmp;
  //     }
  //   }
  // }

  var departs = [];
  var section_8 = get_8_section(name);
  var depart_8 = get_depart_name(section_8);

  // if (depart_8 != '内分泌' && depart_8 != '肾病' && ) {
  if (must_transfer_department.indexOf(depart_8) < 0) {
    departs[0] = '内分泌';
  } else {
    departs[0] = depart_8;
  }

  for (var i = 1; i < 8; i++) {
    var index = (si + i) % 7 + 1;
    var less_depart = get_less_student_count_depart(index, departs, si);
    // var less_depart = get_less_student_count_depart(i, departs);

    if (departs.indexOf(less_depart) > -1) {
      console.dir(departs);
      console.log(index, less_depart);
      console.dir(depart_tmp, {depth: 10});
      throw Error('查询最小depart重复');
    }

    departs[index] = less_depart;
    add_student_in_depart(index, less_depart);
  }

  var random_sections = [];

  for (var i = 0; i < departs.length; i++) {
    if (i == 0 && must_transfer_department_mouths[depart_8] == 2) {
      random_sections[i] = section_8;
    } else {
      random_sections.push(get_random_section_in_depart(departs[i]));
    }
  }

  console.dir(departs)
  console.dir(random_sections)

  return random_sections;
}

// 按照学生，排病区
(function() {
  for (var si = 0; si < students.length; si++) {
    var s_name = students[si];
    var student = students_info[s_name];

    console.log('开始排' + s_name + '的班');

    var random_sections = random_sort_must_depart(student, si);

    // 将两个月的拉长
    for (var i = 0; i < two_mouths_section.length; i++) {
      var tm_depart = two_mouths_section[i];
      var tm_index = random_sections.indexOf(tm_depart);

      if (tm_index > -1) {
        random_sections.splice(tm_index, 0, tm_depart);
      }
    }

    student.sections.push(...random_sections);
    console.dir(student.sections);

    for (var mi = 0; mi < mouth_count; mi++) {
      var cur_section = random_sections[mi];
      var cur_section_student = section_students[mi];

      cur_section_student[cur_section].push(s_name);
    }
  }
})();


// console.dir(students_info, { depth: 10 });
// console.dir(depart_students, { depth: 10 });
console.dir(section_students, { depth: 10 });
console.dir(depart_tmp, { depth: 10 });


// console.log('avg_students_count: ', avg_students_count);

function plain_section(mouth, section_index, section, student) {
  // console.log(mouth, section);
  // console.dir(student, { depth: 10 });

  // console.dir(section_students);
  // console.dir(section_students[mouth]);
  var current_section = section_students[mouth][section];
  // console.log(current_section);
  // 当前学生已选科室数量
  var selected_count = get_sections_count(student);

  if (selected_count - 1 >= mouth) {
    return false;
  }

  // 当前科室已选人数
  var current_count = current_section.length;
  // 当前科室是否必转
  var is_must = is_must_section(section);
  // 当前科室是否选转
  var is_select = is_select_section(section);
  // 当前科室需要待的月数
  var must_mouth_count = get_must_mouth(section);

  // 当前学生是否已选过当前科室
  var is_selected = is_student_selected_section(student, section);
  // 当前学生是否上个月已经选择了当前科室
  var is_pre_mouth_selected = is_student_selected_section_in_pre_mouth(student, section);
  // 当前学生选择当前科室的次数
  var section_selected_count = get_select_section_count(student, section);
  // 上个月选择的科室，是否为需要待两个月的科室
  var is_pre_selected_two_mouth = is_student_pre_selected_two_mouth(student);
  // 上上个月选择的科室，是否为需要待两个月的科室
  var is_pre_pre_selected_two_mouth = is_student_pre_pre_selected_two_mouth(student);
  // 当前学生必转科室数量
  var selected_must_count = get_student_must_count(student);
  // 当前学生选转科室数量
  var selected_select_count = get_student_select_count(student);
  


  // console.log('current_count', current_count, 'is_must', is_must, 'is_select', is_select, 'must_mouth_count', must_mouth_count, 'is_selected', is_selected, 'is_pre_mouth_selected', is_pre_mouth_selected, 'selected_count', selected_count, 'is_pre_selected_two_mouth', is_pre_selected_two_mouth, 'is_pre_pre_selected_two_mouth', is_pre_pre_selected_two_mouth, 'selected_must_count', selected_must_count, 'selected_select_count', selected_select_count);

  var is_plained = false;
  var can_pain = true;
  // 没有排够了人数
  // console.log('current_count', current_count, avg_students_count);
  if (current_count < avg_students_count) {
    // 当前能待一个月，已经选过
    if (must_mouth_count === 1 && is_selected) {
      // console.log(1);
      can_pain = false;
    }

    // 当前能待一个月，没有选过，
    // 当前科室是选转，学生已经没有选转次数
    if (!is_plained && can_pain && must_mouth_count === 1 && !is_selected &&
    is_select && selected_select_count >= 2) {
      // console.log(2);
      can_pain = false;
    }

    // 当前能待两个月，已经选过两个月
    if (!is_plained && can_pain && must_mouth_count === 2 && section_selected_count === 2) {
      // console.log(3);
      can_pain = false;
    }

    // 当前能待两个月, 已经选过一个月
    if (!is_plained && can_pain && must_mouth_count === 2 && is_pre_mouth_selected && section_selected_count === 1) {
      // console.log(4);
      is_plained = true;
    }
  } else {
    // 排够人数了
    // console.log(5555, );
    can_pain = false;
  }

  if (!is_plained && can_pain) {
    is_plained = true;
  }

  if (is_plained) {
    student.sections.push(section);
    current_section.push(student.name);
  }

  return is_plained;
}


