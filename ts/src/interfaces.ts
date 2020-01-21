function demoNormalInterface() {
  interface LabelValues {
    label: string
  }

  function printLable(labelObj: LabelValues):void {
    console.log(labelObj.label);
  }

  printLable({ label: 'this is label' } as LabelValues);
  printLable(<LabelValues>{ label: 'this is another label' });
}

function demoOptionalInterface() {
  interface SquareConfig {
    color?: string,
    width?: number
  }

  function createSquare(config: SquareConfig): void {
    console.log(config);
  }
  createSquare(<SquareConfig>{});
}

function demoReadonlyInterface() {
  interface Point {
    readonly x: number,
    readonly y: number,
  }

  let p1:Point = { x: 1, y: 1 };
  p1.x = 2;
  console.log(p1);

  let ra: ReadonlyArray<number> = [1, 2];
  ra[0] = 2;
  console.log(ra);
}

function demoExcessChecks() {
  interface SquareConfig {
    color?: string,
    width?: number,
    // [x:string]: any
  }

  function createSquare(config: SquareConfig): void {
    console.log(config);
  }

  createSquare({ colour: '写错属性名', width: 100, excess: '额外的属性' });
}

function demoFunctionType() {
  interface SearchFunc {
    (keyword: string): string
  }

  let sf:SearchFunc = function (kw:string):string {
    return kw;
  }
  sf('123');
}

function demoIndexableType() {
  interface StringArray {
    [index: number]: string
  }

  let strArr: StringArray = ['hello'];
  (<Array<string>>strArr).push('world');
  console.log(strArr);
}

function demoHybirdType() {
  interface Counter {
    (start: number): string;
    interval: number;
    reset():void;
  }

  let c:Counter = <Counter>(function(s:number):string { return '' });
  c.interval = 1;
  c.reset = function() {};

  console.log(c);
}

function demo() {
  demoNormalInterface();
  demoOptionalInterface();
  demoReadonlyInterface();
  demoExcessChecks();
  demoFunctionType();
  demoIndexableType();
  demoHybirdType();
}

export = demo;