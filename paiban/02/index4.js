function new_student_info(student_name) {
  var res = {};
  var result = student_result[student_name];

  res['name'] = student_name;
  res['result'] = result.slice();

  var last = last_department.slice();

  for (var i = 0; i < result.length; i++) {
    var ri = last.indexOf(result[i]);

    if (ri > -1) {
      last.splice(ri, 1);
    }
  }
  res['last'] = last;

  return res;
}

function init() {
  var res = {};

  for (var i = 0; i < students.length; i++) {
    var student_name = students[i];
    res[student_name] = new_student_info(student_name);
  }

  return res;
}

// console.dir(JSON.parse(JSON.stringify(plain_students)));

function create_random_depart_group() {
  var res = all_department.slice(2, 8).sort(function(a, b) { return Math.random() > 0.5 ? 1 : -1; });

  res.splice(0, 0, '急诊', '心病科');
  res.push(place_holder_department);

  return res;
}

function create_random_students() {
  var keys = Object.keys(plain_students);

  keys.sort(function () {
    return Math.random() > 0.5 ? 1 : -1;
  });

  return keys;
}

// 非急诊/心病科处理
function plain(mouth, depart) {
  var res = [];
  var mouth_count = depart_count_per_mouth[mouth];
  var keys = Object.keys(plain_students);
  // var keys = create_random_students();

  var count_limit = depart_plain_count[depart];

  for (var i = 0; i < keys.length; i++) {
    var cur_stu_name = keys[i];
    var cur_stu = plain_students[cur_stu_name];
    var result = cur_stu['result'];
    var last = cur_stu['last'];

    if (!cur_stu[mouth]) {
      result[mouth] = place_holder_department;
    }

    // 科室分够人了
    if (mouth_count[depart] >= count_limit) {
      return res;
    }

    // 属于当前科室，直接返回 
    if (student_depart[cur_stu_name] === depart) {
      continue;
    }

    // 当前学生已经分配过科室了
    if (cur_stu[mouth]) {
      continue;
    }

    // 当前同学去过该科室次数
    var in_count = result.filter(function(item) { return item == depart }).length;
    // 当前同学还没去过该科室
    var is_not_in = in_count === 0;

    // 当前学生已经分配过该科室
    if (!is_not_in) {
      continue;
    }

    // 当前同学上月是否急诊/心病科
    var is_pre_2 = result.length > 0 && (two_mouths_depart.indexOf(result[last.length-1]) > -1);
    // 上上月和上月是否相同
    var is_same_2 = result.length > 1 && result[result.length - 2] === result[result.length - 1];

    // 当前科室所在位置, 可能不存在
    var cur_index = last.indexOf(depart);

    var plain_success = function() {
      result[mouth] = depart;
      if (cur_index > -1) {
        last.splice(cur_index, 1);
      }
      mouth_count[depart]++;
      // 当前月已经分配过了
      cur_stu[mouth] = true;
      res.push(cur_stu);
    }

    plain_success();
    continue;
  }

  return res;
}

// 急诊/心病处理
function plain_place_holder(mouth, depart) {
  var res = [];
  var mouth_count = depart_count_per_mouth[mouth];
  var keys = Object.keys(plain_students);
  // var keys = create_random_students();

  for (var i = 0; i < keys.length; i++) {
    var cur_stu_name = keys[i];
    var cur_stu = plain_students[cur_stu_name];
    var result = cur_stu['result'];
    var last = cur_stu['last'];

    // 属于当前科室，直接返回 
    if (student_depart[cur_stu_name] === depart) {
      continue;
    }

    // 当前同学去过该科室次数
    var in_count = result.filter(function(item) { return item == depart }).length;
    // 当前同学还没去过该科室
    var is_not_in = in_count === 0;
    // 上上月和上月是否相同
    var is_same_2 = result.length > 1 && result[result.length - 2] === result[result.length - 1];
    // 上个月科室名，用来判断当前急诊是否和上月急诊一致
    var pre_depart = result[result.length - 1];
    var is_pre_depart_2 = two_mouths_depart.indexOf(pre_depart) > -1;

    // 当前科室所在位置, 可能不存在
    var cur_index = last.indexOf(depart);

    var plain_success = function() {
      result[mouth] = depart;
      if (cur_index > -1) {
        last.splice(cur_index, 1);
      }
      mouth_count[depart]++;
      // 当前月已经分配过了
      cur_stu[mouth] = true;
      res.push(cur_stu);
    }

    // 当前学生已经分配过科室了
    if (cur_stu[mouth]) {
      continue;
    }

    // 已经分配过两次
    if (in_count >= 2) {
      continue;
    }

    // 上个月为急诊/心病， 上上个月不是
    if (pre_depart === depart) {
      plain_success();
      continue
    }
  }

  var keys = Object.keys(plain_students);
  for (var i = 0; i < keys.length; i++) {
    var cur_stu_name = keys[i];
    var cur_stu = plain_students[cur_stu_name];
    var result = cur_stu['result'];
    var last = cur_stu['last'];

    // 属于当前科室，直接返回 
    if (student_depart[cur_stu_name] === depart) {
      continue;
    }

    // 当前同学去过该科室次数
    var in_count = result.filter(function(item) { return item == depart }).length;
    // 当前同学还没去过该科室
    var is_not_in = in_count === 0;
    // 上上月和上月是否相同
    var is_same_2 = result.length > 1 && result[result.length - 2] === result[result.length - 1];
    // 上个月科室名，用来判断当前急诊是否和上月急诊一致
    var pre_depart = result[result.length - 1];
    var is_pre_depart_2 = two_mouths_depart.indexOf(pre_depart) > -1;

    // 当前科室所在位置, 可能不存在
    var cur_index = last.indexOf(depart);

    var plain_success = function() {
      result[mouth] = depart;
      if (cur_index > -1) {
        last.splice(cur_index, 1);
      }
      mouth_count[depart]++;
      // 当前月已经分配过了
      cur_stu[mouth] = true;
      res.push(cur_stu);
    }

    // 当前学生已经分配过科室了
    if (cur_stu[mouth]) {
      continue;
    }

    // 已经分配过两次
    if (in_count >= 2) {
      continue;
    }

    // 上个科室是另一个
    if (is_pre_depart_2 && !is_same_2 && pre_depart !== depart) {
      continue;
    }

    // 科室分够人了
    var limit_count = depart_plain_count[depart];
    if (mouth >= 8) {
      limit_count = 100;
    }
    if (mouth_count[depart] >= limit_count) {
      return res;
    }

    if (is_not_in) {
      plain_success();
      continue;
    }
  }

  return res;
}

function do_plain() {
  for (var i = 2; i < 10; i++) {
    // console.log('第' + (i + 1) + '月');
    var mouth = i;
    var departs = create_random_depart_group();
    var all_students = []
    var placeholser_students = [];
    var mouth_count = depart_count_per_mouth[mouth];

    for (var j = 0; j < departs.length; j++) {
      var depart = departs[j];
      // 当前科室是急诊/心病科
      var is_2 = two_mouths_depart.indexOf(depart) > -1;
      var plain_stds = [];

      if (!is_2) {
        plain_stds = plain(mouth, depart);
      } else {
        plain_stds = plain_place_holder(mouth, depart)
      }
    }
  };
}


var is_success = false;
var count = 10000;
var min_ph = 100000;
var max_ph = -1;
var min_student = null;
var min_per_count = null;

while (count--) {
  console.log('循环' + count);
  var plain_students = init();
  var depart_count_per_mouth = create_depart_count_per_mouth();
  do_plain();

  // console.dir(plain_students);
  // console.dir(depart_count_per_mouth);

  if (check_success()) {
    is_success = true
    break
  }
}


if (is_success) {
  console.log('循环成功');
} else {
  console.log('循环失败');
}

// fix_result();

console.log(min_ph, max_ph);
// console.dir(JSON.stringify(min_student));
// console.dir(JSON.stringify(min_per_count));
console.dir(min_student);
console.dir(min_per_count);


function check_success() {
  var total = 0;
  var keys = Object.keys(plain_students);
  for (var i = 0; i < keys.length; i++) {
    var cur_stu = plain_students[keys[i]];
    var last_length = cur_stu['last'].filter(function(item) { return item !== place_holder_department }).length;
    total += last_length;
  }

  if (total < min_ph) {
    min_ph = total;
    min_student = plain_students;
    min_per_count = depart_count_per_mouth;
  }

  if (max_ph < total) {
    max_ph = total;
  }

  if (total > 0) return false;

  return true;
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