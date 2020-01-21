function demoBoolean() {
  let isDone: boolean = false;
  console.log(isDone);
}

function demoNumber() {
  let decimal: number = 6;
  let hex: number = 0xffff;
  let binary: number = 0b0010;
  let octal: number = 0o77;
  console.log(decimal, hex.toString(16), binary, octal);
}

function demoString() {
  let color: string = 'red';
  console.log(color);

  let tmpstr: string = `color is ${color}`;
  console.log(tmpstr);
}

function demoArray() {
  let list: Array<number> = [1, 2, 3];
  console.log(list);
}

function demoTuple() {
  let x: [string, number] = ['hello', 42];
  console.log(x);
}

function demoEnum() {
  enum Color {Red = 1, Green, Blue};
  let color: Color = Color.Red;
  console.log(color, Color.Blue);
}

function demoAny() {
  let notSure: any = 'this is string';
  console.log(notSure);
  notSure = 42;
  console.log(notSure);
}

function demoVoid() {
  function warnUser():void {
    return;
  }
  console.log(warnUser());
}

function demoNullAndUndefined() {
  let u: undefined = undefined;
  let n: null = null;
  console.log(u, n);
}

function demoNever() {
  function error():never {
    throw new Error('never return');
  }

  try {
    error();
  } catch (error) {
    console.log(error);
  }
}

function demoObject() {
  function create(o:object | null):void {};
  create({ name: '' });
  create(null);
  create(false);
  create(42);
}

function demoTypeAssertions() {
  let someValue: any = 'this is string';
  let strLen: number = (<string>someValue).length;
  let strLen2: number = (someValue as string).length;
  console.log(strLen, strLen2);
}

function demo() {
  demoBoolean();
  demoNumber();
  demoString();
  demoArray();
  demoTuple();
  demoEnum();
  demoAny();
  demoVoid();
  demoNullAndUndefined();
  demoNever();
  demoObject();
  demoTypeAssertions();
}

export = demo;