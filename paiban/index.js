var must_transfer_department = ['急诊', '心病科', 'ICU', '肝胆脾胃病科', '肺病科', '脑病科', '肾病', '内分泌'];
var select_transfer_department = ['老年病'];
// var must_transfer_department = ['急诊', '心病科', 'ICU', '肝胆脾胃病科', '肺病科', '脑病科'];
// var select_transfer_department = ['肾病', '内分泌', '老年病', '肿瘤', '血液科'];

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
  '肺病科': ['肺病'],
  '急诊': ['急诊'],
  'ICU': ['ICU'],
  '肾病': ['肾病'],
  '血液科': ['血液'],
  '内分泌': ['内分泌'],
  '肿瘤': ['肿瘤一区', '肿瘤二区', '肿瘤三区'],
  '老年病': ['老年病'],
}

var transfer_section_arr = [];
var transfer_section_info = {};

(function() {
  var department_sections_keys = Object.keys(department_sections);
  
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

console.dir(transfer_section_arr);
console.dir(transfer_section_info, { depth: 10 });

function is_must_department(section) {
  return transfer_section_info[section].is_must;
}

function is_select_department(section) {
  return transfer_section_info[section].is_select;
}

function get_must_mouth(section) {
  return transfer_section_info[section].must_mouth;
}


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
  "介睿峥": ["肺病"],
  "苏珊珊": ["肺病"],
  "邱月清": ["肺病"],
  "李英宵": ["肺病"],
  "樊亚芳": ["肺病"],
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

var students = ["成家宏","邢玉凤","马瑞红","侯学文","朱丹娜","崔艳粉","张创业","孟六阳","张迪","潘海涛","赵永华","张超","刘建申","莫万灵","胡颖","贺群慧","王露","段启","代云","王棣丞","任闪闪","李锋森","范莹莹","李登科","介睿峥","苏珊珊","邱月清","李英宵","樊亚芳","李治兵","李习婉","王若凡","李倩倩","任娟","张鑫丽","袁成凤","郑璐璐","娄方敏","叶子","王红艳","张亚乐","黄爱娟","任宗浩","吉兰洁","李颖","张静晓","袁帆","侯露阳","张璐鹏","张开波","康研","李方方","邵帅","陈梦利"];

var students_info = {};

(function() {
  for (var i = 0; i < students.length; i++) {
    students_info[students[i]] = {
      name: students[i],
      sections: [...results_8[students[i]]],
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
  var musts = sections.filter(function(item) { return is_must_department(item); });

  return musts.length;
}

function get_student_select_count(student) {
  var sections = student.sections;
  var selects = sections.filter(function(item) { return is_select_department(item); });

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

function new_section_students() {
  var res = {};
  for (var i = 0; i < transfer_section_arr.length; i++) {
    res[transfer_section_arr[i]] = [];
  }

  return res;
}

(function() {
  for (var i = 0; i < mouth_count; i++) {
    section_students[i] = new_section_students();
  }

  var first_section_students = section_students[0];
  var keys = Object.keys(results_8);

  for (var i = 0; i < keys.length; i++) {
    var sections = results_8[keys[i]];
    first_section_students[sections[0]].push(keys[i]);
  }
})();

console.dir(section_students);

// 平均每个科室可以排多少个同学
var avg_students_count = Math.floor(students.length / transfer_section_arr.length);

// 一次排9个月的班
(function() {
  var current_section = null;
  var current_mouth = null;
  for (var i = 1; i < mouth_count; i++) {
    current_mouth = i;
    console.log('开始排第个' + current_mouth + '月的班');

    for (var j = 0; j < transfer_section_arr.length; j++) {
      current_section = transfer_section_arr[j];
      // console.log('开始排科室' + current_section + '的班');
      // var random_students = students.slice();
      // random_students.sort();
      // 当前科室索引
      // 已排学生数量

      var plain_count = 0;
      for (var s = 0; s < students.length; s++) {
        if (plain_section(current_mouth, j, current_section, students_info[students[s]])) {
          plain_count += 1;
        }
      }
      console.log('科室' + current_section + '排了' + plain_count + '人');
    }
  }
})();



console.dir(students_info, { depth: 10 })
console.dir(section_students, { depth: 10 })

console.log('avg_students_count: ', avg_students_count);

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
  var is_must = is_must_department(section);
  // 当前科室是否选转
  var is_select = is_select_department(section);
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


