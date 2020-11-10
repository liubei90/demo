function new_student_info(student_name) {
  var res = {};
  var result = student_result[student_name];

  res['name'] = student_name;
  res['result'] = result.slice();

  var last = all_department.slice();

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

var plain_students = init();

function create_random_depart_group() {
  var res = all_department.slice().sort(function(a, b) { 
    return Math.random() > 0.5 ? 1 : -1;
  });
  var pli = res.indexOf(place_holder_department);
  var tmp = res[pli];

  res[pli] = res[res.length - 1];
  res[res.length - 1] = tmp;

  return res;
}

function create_random_students() {
  var keys = Object.keys(plain_students);

  keys.sort(function(a, b) {
    var ca = plain_students[a];
    var cb = plain_students[b];

    var result_a = ca['result'];
    var result_b = cb['result'];

    var count_2_a = result_a.filter(function(item) { return two_mouths_depart.indexOf(item) > -1 }).length;
    var count_2_b = result_b.filter(function(item) { return two_mouths_depart.indexOf(item) > -1 }).length;

    return count_2_a > count_2_b ? -1 : 1;
  });

  return keys;

  // for (var i = 0; i < keys.length; i++) {
  //   ;
  // }
}

// 非急诊/心病科处理
function plain(mouth, depart) {
  var res = [];
  var mouth_count = depart_count_per_mouth[mouth];
  // var keys = Object.keys(plain_students);

  var keys = create_random_students();

  for (var i = 0; i < keys.length; i++) {
    // 科室分够人了
    if (mouth_count[depart] >= depart_plain_count[depart]) {
      return res;
    }

    var cur_stu_name = keys[i];
    var cur_stu = plain_students[cur_stu_name];
    var result = cur_stu['result'];
    var last = cur_stu['last'];

    // 当前学生已经分配过科室了
    if (cur_stu[mouth]) {
      continue;
    }

    // // 当前同学上上月是否急诊/心病科
    var is_pre_pre_2 = result.length > 1 && (two_mouths_depart.indexOf(result[last.length-2]) > -1);
    // 当前同学上月是否急诊/心病科
    var is_pre_2 = result.length > 0 && (two_mouths_depart.indexOf(result[last.length-1]) > -1);
    // 上上月和上月是否相同
    var is_same_2 = result.length > 1 && result[result.length - 2] === result[result.length - 1];
    // 上个月科室名，用来判断当前急诊是否和上月急诊一致
    var pre_depart = result[result.length - 1];
    // 当前同学去过该科室次数
    var in_count = result.filter(function(item) { return item == depart }).length;
    // 当前同学还没去过该科室
    var is_not_in = in_count === 0;

    // 当前科室所在位置, 可能不存在
    var cur_index = last.indexOf(depart);

    var plain_success = function() {
      result.push(depart);
      last.splice(cur_index, 1);
      mouth_count[depart]++;
      // 当前月已经分配过了
      cur_stu[mouth] = true;
      res.push(cur_stu);
    }

    // 上月为急诊/心病，且上上月不为急诊/心病
    if (depart === place_holder_department || (is_not_in && (!is_pre_2 || is_same_2))) {
      plain_success();
      continue;;
    }

    // if (is_not_in || ) {
    //   // 非急诊没有排满，也可以上
    //   plain_success();
    //   continue;
    // }
  }

  return res;
}

// 急诊/心病处理
function plain_place_holder(mouth, placeholser_students) {
  var mouth_count = depart_count_per_mouth[mouth];

  // 判断是否急诊/心病人数合适
  for (var m = 0; m < two_mouths_depart.length; m++) {
    var td = two_mouths_depart[m];
    var lower_count = depart_plain_count[td] - mouth_count[td];
    for (var n = 0; n < placeholser_students.length; n++) {
      var c_s = placeholser_students[n];
      var result = c_s['result'];
      var last = c_s['last'];
      // console.dir(c_s);
      // 当月已经分配过
      if (c_s[mouth] === 2) {
        continue;
      }

      // 已经分配够了
      if (lower_count <= 0) {
        continue;
      }

      // 上个月科室名，用来判断当前急诊是否和上月急诊一致
      var pre_depart = result[result.length - 1];
      // 将急诊/心病放入
      var in_count = result.filter(function(item) { return item == td }).length;

      if ((in_count === 1 && pre_depart === td) || in_count === 0) {
        c_s[mouth] = 2;
        lower_count--;
        // // 移除结果
        var pi = result.indexOf(place_holder_department);
        result.splice(pi, 1);
        // 还原占位
        last.push(place_holder_department);
        mouth_count[place_holder_department]--;

        // 加入急诊/心病
        result.push(td);
        var rdi = last.indexOf(td);
        last.splice(rdi, 1);
        mouth_count[td]++;
      }
    }
  }
}

function do_plain() {
  for (var i = 2; i < 10; i++) {
    console.log('第' + (i + 1) + '月');
    var mouth = i;
    var departs = create_random_depart_group();
    var all_students = []
    var placeholser_students = [];

    for (var j = 0; j < departs.length; j++) {
      var depart = departs[j];
      // 当前科室是急诊/心病科
      var is_2 = two_mouths_depart.indexOf(depart) > -1;
      var plain_stds = [];

      if (!is_2) {
        plain_stds = plain(mouth, depart);
      }

      if (depart === place_holder_department) {
        placeholser_students.push(...plain_stds);
      }
      all_students.push(...plain_stds);
    }

    console.dir(all_students.length);

    plain_place_holder(mouth, placeholser_students)

    console.dir(placeholser_students);
  };
}
do_plain();

console.dir(plain_students);
console.dir(depart_count_per_mouth);