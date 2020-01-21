function demoFunctionType() {
  let add: (a: number, b:number) => number = 
    function(a:number, b:number):number { return a + b; };

  console.log(add(1, 2));
}

function demoFunctionParams() {
  function buildName(firstName:string, lastName?:string):string {
    return firstName + ' ' + lastName;
  }

  console.log(buildName('hello'));

  function buildName2(firstName:string, lastName:string = 'jek'):string {
    return firstName + ' ' + lastName;
  }

  console.log(buildName2('hello'));

  function buildName3(firstName:string, ...rest: string[]):string {
    return firstName + ' ' + rest.join(' ');
  }

  console.log(buildName3('hello', 'a', 'b'));
}

function demoFunctionThis() {
  class Handler {
    info:string = 'handler';
    onClick:(e:string) => void = (e:string): void => { console.log(this.info, e) };
  }

  let h:Handler = new Handler();
  h.onClick('hi');
}

function demoFunctionOverloads() {
  function doSthing(x:number):void
  function doSthing(x:string):string
  function doSthing(x:any):any {
    if (typeof x === 'string') {
      return x;
    }
  }

  console.log(doSthing('abc'));
  console.log(doSthing(1));
}

function demo() {
  demoFunctionType();
  demoFunctionParams();
  demoFunctionThis();
  demoFunctionOverloads();
}

export = demo;