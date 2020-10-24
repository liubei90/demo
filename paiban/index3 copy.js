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

function plain(mouth, depart) {
  var count = 0;
  var pre_pre_mouth_count = depart_count_per_mouth[mouth - 2];
  var pre_mouth_count = depart_count_per_mouth[mouth - 1];
  var mouth_count = depart_count_per_mouth[mouth];
  var placeholser_students = [];
  // 当前科室是急诊/心病科
  var is_2 = two_mouths_depart.indexOf(depart) > -1;

  var keys = Object.keys(plain_students);

  for (var i = 0; i < keys.length; i++) {
    // 科室分够人了
    if (count >= depart_plain_count[depart]) {
      return;
    }

    var cur_stu_name = keys[i];
    var cur_stu = plain_students[cur_stu_name];
    var result = cur_stu['result'];
    var last = cur_stu['last'];

    // 当前同学上上月是否急诊/心病科
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

    function plain_success() {
      result.push(depart);
      last.splice(cur_index, 1);
      mouth_count[depart]++;

      if (depart === place_holder_department) {
        placeholser_students.push(cur_stu);
      }
    }

    // 急诊/心病连续上
    if (is_2) {
      // // 上上个月不是急诊/心病，上个月是急诊/心病, 
      // // 上月是急诊，本月也是急诊。 或者上月是心病，本月也是心病
      // if (!is_pre_pre_2 && is_pre_2 
      //   && pre_depart === depart) {
      //   plain_success();
      //   continue;
      // } else if (is_pre_pre_2 && is_pre_2 && !is_same_2 
      //   && pre_depart === depart) {
      //   // 上个月是急诊/心病 上上月是心病/急诊
      //   // 上月是急诊，本月也是急诊。 或者上月是心病，本月也是心病
      //   plain_success();
      //   continue;
      // } else {
      //   // 当前情况下不做分配，都放到内分泌，等排完后看是否急诊/心病人数合适，再从内分泌调整
      // }

      // 如果上过该科室一次，且为最后一次
      if (in_count === 1 && pre_depart === depart) {
        plain_success();
        continue;
      } else {
        // 上过2次，不做排课
        // 或者没有上过，不做处理，等排完后看是否急诊/心病人数合适，再从内分泌调整
      }
    } else {
      if (is_not_in) {
        // 非急诊没有排满，也可以上
        plain_success();
        continue;
      } else {
        // 非急诊，已经排过，不做处理
      }
    }
  }

  // 判断是否急诊/心病人数合适
  if (is_2) {
    for (var i = 0; i < two_mouths_depart.length; i++) {
      var td = two_mouths_depart[i];
      var lower_count = depart_plain_count[td] - mouth_count[td];

      if (lower_count > 0) {
        for (var j = 0; j < lower_count; j++) {
          var jz_s = placeholser_students.shift();
          if (jz_s) {
            var result = jz_s['result'];
            var last = jz_s['last'];
            // 移除结果
            var pi = result.indexOf(place_holder_department);
            result.splice(pi, 1);
            // 还原内分泌
            last.push(place_holder_department);
            mouth_count[place_holder_department]--;

            // 将急诊/心病放入
            var in_count = result.filter(function(item) { return item == td }).length;
            if (in_count === 0) {
              result.push(td);
              var rdi = last.indexOf(td);
              td.splice(rdi, 1);
              mouth_count[td]++;
            }
          }
        }
      }
    }
  }
}

function do_plain() {
  for (var i = 2; i < 10; i++) {
    var mouth = i;
    var departs = create_random_depart_group();

    for (var j = 0; j < departs.length; j++) {
      var depart = departs[j];

      plain(mouth, depart);
    }
  };
}

console.log(plain_students);
