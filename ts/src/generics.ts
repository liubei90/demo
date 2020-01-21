function demoGenericsBasic() {
  function identity<T>(arg:T):T {
    return arg;
  }

  console.log(identity<number>(1));
  console.log(identity('hello'));
}

function demoGenericsTypes() {
  interface identityFn {
    <T>(arg:T):T
  }

  function identity<T>(arg:T):T {
    return arg;
  }

  let func: <T>(arg:T) => T = identity;
  console.log(func(1));

  let func2:identityFn = identity;
  console.log(func2('hello'));

  interface indentityFn2<T> {
    (arg:T):T;
  }

  let func3:indentityFn2<string> = identity;
  console.log(func3('world'));
  console.log(func3(2));
}

function demoGenericConstraints() {
  interface Lengthwise {
    length: number
  }

  function identity<T extends Lengthwise>(arg: T): T {
    // console.log(arg.length);
    return { length: arg.length * 2 } as T;
  }

  console.log(identity({length: 1}));
}

function demo() {
  demoGenericsBasic();
  demoGenericsTypes();
  demoGenericConstraints();
}

export = demo;