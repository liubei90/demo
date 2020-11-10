var place_holder_department = 'zanwei';

var two_mouths_depart = ['急诊', '心病科'];

var all_department = ['急诊', '心病科', 'ICU', '肝胆脾胃病科', '肺病科', '脑病科', '肾病', '内分泌', 'zanwei'];

var last_department = ['急诊', '急诊', '心病科', '心病科', 'ICU', '肝胆脾胃病科', '肺病科', '脑病科', '肾病', '内分泌', 'zanwei'];


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
};

var depart_plain_count = {
  '急诊': 11, 
  '心病科': 9, 
  'ICU': 6, 
  '肝胆脾胃病科': 6, 
  '肺病科': 6, 
  '脑病科': 5,
  '肾病': 3,
  '内分泌': 6,
  'zanwei': 100,
};

function create_depart_count_per_mouth() {
  return [
    {
      'index': 1,
      '急诊': 7, 
      '心病科': 8, 
      'ICU': 4, 
      '肝胆脾胃病科': 7, 
      '肺病科': 5, 
      '脑病科': 9,
      '内分泌': 2,
      '肾病': 4,
      'zanwei': 0,
    }, // 1
    {
      'index': 2,
      '急诊': 11, 
      '心病科': 8, 
      'ICU': 6, 
      '肝胆脾胃病科': 5, 
      '肺病科': 5, 
      '脑病科': 6,
      '内分泌': 5,
      '肾病': 3,
      'zanwei': 0,
    }, // 2
    create_depart_count(3),
    create_depart_count(4),
    create_depart_count(5),
    create_depart_count(6),
    create_depart_count(7),
    create_depart_count(8),
    create_depart_count(9),
    create_depart_count(10),
  ];
}

// var depart_count_per_mouth = ;

function create_depart_count(index) {
  var res = {
    'index': index
  };

  for (var i = 0; i < all_department.length; i++) {
    res[all_department[i]] = 0;
  }

  return res;
}