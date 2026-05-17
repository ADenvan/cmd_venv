---
name: js-functional
description: |
  JavaScript functional programming expert specializing in pure functions, 
  function composition, immutability, effect management, and functional patterns.
  
  Use when: "чистые функции", "функциональная композиция", "управление состоянием", 
  "immutability", "функции высшего порядка", "монады", "Either/Result типы", 
  "обработка ошибок без try-catch", "управление эффектами", "тестируемый код", 
  "pure functions", "function composition", "higher-order functions", 
  "functional state management", "effect handling", "error handling without exceptions"
---

# JavaScript Functional Programming

Expert guide for writing robust, testable JavaScript code using functional programming principles: pure functions, immutability, composition, and effect management.

## When to Use This Skill

This skill is essential when:

- **Refactoring to Functional Style**: Converting imperative code to functional patterns
- **Managing State**: Building predictable state management without mutations
- **Composing Logic**: Creating reusable, composable function pipelines
- **Handling Errors**: Using Result/Either types instead of exceptions
- **Managing Side Effects**: Isolating IO and side effects from pure logic
- **Writing Testable Code**: Achieving 100% testable pure functions
- **CLI Tooling**: Functional patterns for process management and streams
- **Data Processing**: Transforming data through functional pipelines

## Quick Start

### 1. Pure Functions & Immutability

```javascript
// PURE: Same input → Same output, no side effects
const calculateTotal = (items) =>
  items.reduce((sum, item) => sum + item.price * item.quantity, 0);

// IMMUTABLE: Never mutate, always return new
const addItem = (cart, item) => ({
  ...cart,
  items: [...cart.items, item],
  updatedAt: Date.now()
});

// USAGE
const cart = { items: [], updatedAt: 0 };
const newCart = addItem(cart, { id: 1, price: 10, quantity: 2 });
// cart is unchanged!
```

### 2. Function Composition (pipe & compose)

```javascript
// pipe: left to right
const pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);

// compose: right to left  
const compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);

// EXAMPLE: Data transformation pipeline
const processData = pipe(
  (data) => data.filter((x) => x.active),
  (data) => data.map((x) => ({ ...x, score: x.score * 2 })),
  (data) => data.sort((a, b) => b.score - a.score),
  (data) => data.slice(0, 10)
);

const topActiveUsers = processData(users);
```

### 3. Higher-Order Functions

```javascript
// Function factory
const createMultiplier = (factor) => (x) => x * factor;
const double = createMultiplier(2);
const triple = createMultiplier(3);

// Function decorator (wrapper)
const withLogging = (fn) => (...args) => {
  console.log(`Calling ${fn.name} with`, args);
  const result = fn(...args);
  console.log(`Result:`, result);
  return result;
};

const loggedAdd = withLogging((a, b) => a + b);
```

### 4. Error Handling with Result Type

```javascript
// Result type: { ok: boolean, value?: any, error?: string }
const Ok = (value) => ({ ok: true, value });
const Err = (error) => ({ ok: false, error });

// Safe division
const safeDivide = (a, b) =>
  b === 0 ? Err("Division by zero") : Ok(a / b);

// Chaining results
const result = safeDivide(10, 2)
  .andThen((x) => safeDivide(x, 5))
  .map((x) => x * 10);

// Pattern matching
if (result.ok) {
  console.log("Success:", result.value);
} else {
  console.error("Error:", result.error);
}
```

### 5. Effect Management (IO Monad Pattern)

```javascript
// IO: Lazy, composable side effects
const IO = (effect) => ({
  map: (fn) => IO(() => fn(effect())),
  flatMap: (fn) => IO(() => fn(effect()).run()),
  run: effect
});

// Pure logic stays pure
const readFile = (path) => IO(() => require("fs").readFileSync(path, "utf8"));
const parseJSON = (str) => IO(() => JSON.parse(str));
const writeFile = (path, data) =>
  IO(() => {
    require("fs").writeFileSync(path, JSON.stringify(data));
    return path;
  });

// Compose effects without executing
const processConfig = (inputPath, outputPath) =>
  readFile(inputPath).flatMap(parseJSON).flatMap((config) =>
    writeFile(outputPath, { ...config, processed: true })
  );

// Execute only at the edge
processConfig("config.json", "output.json").run();
```

## Core Concepts

### Pure Functions

A function is pure if:
1. **Deterministic**: Same input always produces same output
2. **No Side Effects**: Doesn't modify external state

```javascript
// IMPURE (avoid)
let counter = 0;
const increment = () => ++counter; // Modifies external state

// PURE (prefer)
const increment = (counter) => counter + 1; // Returns new value

// IMPURE
const getCurrentTime = () => Date.now(); // Non-deterministic

// PURE (with explicit dependency injection)
const getTime = (now) => now; // Deterministic when passed time
```

### Immutability Patterns

```javascript
// Objects: spread operator
const updateUser = (user, updates) => ({ ...user, ...updates });

// Arrays: never use push, pop, splice
const append = (arr, item) => [...arr, item];
const prepend = (arr, item) => [item, ...arr];
const removeAt = (arr, index) => [...arr.slice(0, index), ...arr.slice(index + 1)];
const updateAt = (arr, index, fn) =>
  arr.map((item, i) => (i === index ? fn(item) : item));

// Nested updates with lenses pattern
const setPath = (obj, path, value) => {
  const [head, ...tail] = path;
  return tail.length === 0
    ? { ...obj, [head]: value }
    : { ...obj, [head]: setPath(obj[head], tail, value) };
};

// Usage
const user = { profile: { address: { city: "NYC" } } };
const updated = setPath(user, ["profile", "address", "city"], "LA");
```

### Function Composition Patterns

```javascript
// Point-free style (tacit programming)
const users = [
  { name: "Alice", age: 25, active: true },
  { name: "Bob", age: 30, active: false },
  { name: "Carol", age: 28, active: true }
];

// Instead of:
const getActiveNames = (users) =>
  users.filter((u) => u.active).map((u) => u.name);

// Point-free:
const filter = (predicate) => (arr) => arr.filter(predicate);
const map = (fn) => (arr) => arr.map(fn);
const prop = (key) => (obj) => obj[key];
const equals = (value) => (x) => x === value;

const getActiveNames = pipe(
  filter(pipe(prop("active"), equals(true))),
  map(prop("name"))
);
```

### Functors

A Functor is anything that implements `map`:

```javascript
// Array is a Functor
[1, 2, 3].map((x) => x * 2); // [2, 4, 6]

// Maybe Functor (handling null/undefined)
const Maybe = (value) => ({
  map: (fn) => (value == null ? Maybe(null) : Maybe(fn(value))),
  filter: (predicate) =>
    value == null || !predicate(value) ? Maybe(null) : Maybe(value),
  getOrElse: (defaultValue) => (value == null ? defaultValue : value),
  value
});

// Usage
const user = { address: { city: "NYC" } };
const city = Maybe(user)
  .map((u) => u.address)
  .map((a) => a.city)
  .getOrElse("Unknown");

// Result Functor (for error handling)
const Result = {
  Ok: (value) => ({
    map: (fn) => Result.Ok(fn(value)),
    flatMap: (fn) => fn(value),
    fold: (onError, onSuccess) => onSuccess(value),
    isOk: true,
    isErr: false,
    value
  }),
  Err: (error) => ({
    map: () => Result.Err(error),
    flatMap: () => Result.Err(error),
    fold: (onError) => onError(error),
    isOk: false,
    isErr: true,
    error
  })
};
```

## Collection Processing

### Transducers (Composable Transformations)

```javascript
// Basic transducer
const map = (fn) => (reducer) => (acc, item) => reducer(acc, fn(item));
const filter = (predicate) => (reducer) => (acc, item) =>
  predicate(item) ? reducer(acc, item) : acc;

// Compose transducers
const xform = pipe(
  filter((x) => x.active),
  map((x) => x.score)
);

// Apply to reduce
const transduce = (xform, reducer, init, arr) =>
  arr.reduce(xform(reducer), init);

const totalScore = transduce(
  xform,
  (sum, score) => sum + score,
  0,
  users
);
```

### Lazy Evaluation with Generators

```javascript
function* range(start, end) {
  for (let i = start; i < end; i++) yield i;
}

function* map(iter, fn) {
  for (const x of iter) yield fn(x);
}

function* filter(iter, predicate) {
  for (const x of iter) if (predicate(x)) yield x;
}

function* take(iter, n) {
  let count = 0;
  for (const x of iter) {
    if (count >= n) return;
    yield x;
    count++;
  }
}

// Lazy pipeline - nothing computed yet
const pipeline = take(
  filter(
    map(range(1, 1000000), (x) => x * x),
    (x) => x % 2 === 0
  ),
  5
);

// Only compute what's needed
console.log([...pipeline]); // [4, 16, 36, 64, 100]
```

## Asynchronous Functional Programming

### Async Composition

```javascript
const asyncPipe = (...fns) => (x) =>
  fns.reduce(async (v, f) => f(await v), x);

const asyncCompose = (...fns) => (x) =>
  fns.reduceRight(async (v, f) => f(await v), x);

// Example
const fetchUser = async (id) => {
  const res = await fetch(`/api/users/${id}`);
  return res.json();
};

const validateUser = (user) =>
  user.active ? Result.Ok(user) : Result.Err("User inactive");

const getUserPermissions = async (user) => {
  const res = await fetch(`/api/permissions/${user.id}`);
  return { ...user, permissions: await res.json() };
};

const loadUserData = asyncPipe(fetchUser, getUserPermissions);
```

### AsyncResult Type

```javascript
const AsyncResult = (promise) => ({
  map: (fn) => AsyncResult(promise.then((r) => r.map(fn))),
  flatMap: (fn) =>
    AsyncResult(
      promise.then((r) => (r.isOk ? fn(r.value).promise : Promise.resolve(r)))
    ),
  fold: (onError, onSuccess) => promise.then((r) => r.fold(onError, onSuccess)),
  promise
});

AsyncResult.of = (promise) =>
  AsyncResult(
    promise.then(
      (value) => Result.Ok(value),
      (error) => Result.Err(error)
    )
  );

// Usage
const fetchWithResult = (url) =>
  AsyncResult.of(fetch(url).then((r) => r.json()));

fetchWithResult("/api/data")
  .map((data) => data.items)
  .flatMap((items) =>
    AsyncResult.of(Promise.all(items.map(fetchDetails)))
  )
  .fold(
    (err) => console.error("Failed:", err),
    (data) => console.log("Success:", data)
  );
```

## CLI and Process Management

### Pure Process Spawning

```javascript
const { spawn } = require("child_process");
const { promisify } = require("util");

// IO-wrapped process execution
const execCommand = (command, args = [], options = {}) =>
  IO(() => {
    return new Promise((resolve, reject) => {
      const proc = spawn(command, args, options);
      let stdout = "";
      let stderr = "";

      proc.stdout.on("data", (data) => (stdout += data));
      proc.stderr.on("data", (data) => (stderr += data));

      proc.on("close", (code) =>
        code === 0
          ? resolve({ code, stdout, stderr })
          : reject(new Error(`Process exited with code ${code}: ${stderr}`))
      );
    });
  });

// Composable process pipeline
const runTests = () => execCommand("npm", ["test"]);
const runBuild = () => execCommand("npm", ["run", "build"]);

const ciPipeline = runTests().flatMap((result) =>
  result.code === 0 ? runBuild() : IO(() => Promise.reject("Tests failed"))
);
```

### Stream Processing

```javascript
const { createReadStream } = require("fs");
const { createInterface } = require("readline");

// Functional stream processing
const processLines = (filePath, transform) =>
  IO(() => {
    const stream = createReadStream(filePath);
    const rl = createInterface({ input: stream });

    const results = [];
    rl.on("line", (line) => {
      const result = transform(line);
      if (result.isOk) results.push(result.value);
    });

    return new Promise((resolve) => {
      rl.on("close", () => resolve(results));
    });
  });

// Usage
const parseLogLine = (line) => {
  try {
    return Result.Ok(JSON.parse(line));
  } catch (e) {
    return Result.Err(`Invalid JSON: ${line}`);
  }
};

processLines("app.log", parseLogLine).run().then(console.log);
```

## Error Handling Patterns

### Railway-Oriented Programming

```javascript
// Chain operations that can fail
const validateEmail = (email) =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
    ? Result.Ok(email)
    : Result.Err("Invalid email format");

const checkDomain = (email) =>
  email.endsWith("@company.com")
    ? Result.Ok(email)
    : Result.Err("Only company emails allowed");

const createUser = (email) => Result.Ok({ id: generateId(), email });

// Railway switching
const registerUser = (email) =>
  Result.Ok(email)
    .flatMap(validateEmail)
    .flatMap(checkDomain)
    .flatMap(createUser);

// Handle both tracks
registerUser("user@company.com").fold(
  (error) => ({ success: false, error }),
  (user) => ({ success: true, user })
);
```

### Validation Combinators

```javascript
const all = (...validators) => (value) => {
  const errors = validators
    .map((v) => v(value))
    .filter((r) => r.isErr)
    .map((r) => r.error);

  return errors.length === 0 ? Result.Ok(value) : Result.Err(errors);
};

const minLength = (n) => (str) =>
  str.length >= n
    ? Result.Ok(str)
    : Result.Err(`Must be at least ${n} characters`);

const maxLength = (n) => (str) =>
  str.length <= n
    ? Result.Ok(str)
    : Result.Err(`Must be at most ${n} characters`);

const required = (value) =>
  value != null && value !== ""
    ? Result.Ok(value)
    : Result.Err("Required field");

// Compose validators
const validatePassword = all(required, minLength(8), maxLength(128));

validatePassword("short"); // Err(["Must be at least 8 characters"])
validatePassword("validpassword123"); // Ok("validpassword123")
```

## Testing Strategies

### Pure Functions are Trivial to Test

```javascript
// No mocks needed, no setup, no cleanup
const add = (a, b) => a + b;
const calculateDiscount = (price, rate) => price * (1 - rate);

// Tests
expect(add(2, 3)).toBe(5);
expect(calculateDiscount(100, 0.2)).toBe(80);
```

### Dependency Injection for Effects

```javascript
// Instead of direct dependencies
const saveUserBad = (user) => {
  const db = require("./db"); // Hidden dependency!
  return db.users.insert(user);
};

// Inject dependencies
const saveUser = (db) => (user) => db.users.insert(user);

// Test with mock
const mockDb = {
  users: {
    insert: jest.fn((user) => Promise.resolve({ id: 1, ...user }))
  }
};

await saveUser(mockDb)({ name: "Alice" });
expect(mockDb.users.insert).toHaveBeenCalledWith({ name: "Alice" });
```

### Property-Based Testing

```javascript
const fc = require("fast-check");

// Test properties, not examples
fc.assert(
  fc.property(fc.integer(), fc.integer(), (a, b) => {
    // Commutativity: a + b === b + a
    expect(add(a, b)).toBe(add(b, a));

    // Associativity: (a + b) + c === a + (b + c)
    const c = fc.sample(fc.integer(), 1)[0];
    expect(add(add(a, b), c)).toBe(add(a, add(b, c)));

    // Identity: a + 0 === a
    expect(add(a, 0)).toBe(a);
  })
);
```

## Common Patterns

### Memoization

```javascript
const memoize = (fn) => {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
};

const fibonacci = memoize((n) =>
  n <= 1 ? n : fibonacci(n - 1) + fibonacci(n - 2)
);

console.log(fibonacci(50)); // Fast!
```

### Currying

```javascript
const curry = (fn) =>
  function curried(...args) {
    return args.length >= fn.length
      ? fn.apply(this, args)
      : (...next) => curried(...args, ...next);
  };

const add = curry((a, b, c) => a + b + c);

add(1)(2)(3); // 6
add(1, 2)(3); // 6
add(1)(2, 3); // 6
add(1, 2, 3); // 6
```

### Thunk (Lazy Evaluation)

```javascript
// Thunk: () => value (delayed computation)
const thunk = (fn) => () => fn();

const expensive = thunk(() => {
  console.log("Computing...");
  return Math.random() * 1000;
});

const value1 = expensive(); // "Computing...", random value
const value2 = expensive(); // "Computing...", different value

// Memoized thunk
const memoThunk = (fn) => {
  let computed = false;
  let result;
  return () => {
    if (!computed) {
      result = fn();
      computed = true;
    }
    return result;
  };
};

const lazyValue = memoThunk(expensive());
lazyValue(); // Computes once
lazyValue(); // Returns cached value
```

## Anti-Patterns to Avoid

### 1. Mixed Paradigms

```javascript
// BAD: Mixing imperative and functional
const processItems = (items) => {
  const result = [];
  for (let i = 0; i < items.length; i++) {
    // Imperative loop
    const transformed = items[i].value * 2; // Direct mutation
    if (transformed > 10) {
      result.push(transformed); // Side effect
    }
  }
  return result;
};

// GOOD: Pure functional
const processItems = pipe(
  map((item) => item.value * 2),
  filter((x) => x > 10)
);
```

### 2. Hidden Side Effects

```javascript
// BAD: Hidden mutation
const addTimestamp = (obj) => {
  obj.timestamp = Date.now(); // Mutation!
  return obj;
};

// GOOD: Explicit return
const addTimestamp = (obj) => ({
  ...obj,
  timestamp: Date.now()
});
```

### 3. Over-Engineering

```javascript
// BAD: Unnecessary abstraction
const getUserName = pipe(
  (id) => ({ id }),
  (obj) => ({ ...obj, type: "user" }),
  (obj) => db.find(obj),
  (user) => user?.name
);

// GOOD: Simple and clear
const getUserName = (id) => db.find({ id, type: "user" })?.name;
```

## Best Practices Summary

1. **Prefer `const`**: Never use `let` or `var` for values that don't change
2. **Pure Functions**: Extract impure operations to the edges
3. **Small Functions**: < 20 lines, single responsibility
4. **Compose, Don't Nest**: Flat pipelines over deep nesting
5. **Explicit Over Implicit**: Pass dependencies, don't hide them
6. **Type Safety**: Use JSDoc or TypeScript for function contracts
7. **Test Pure Logic**: Aim for 100% pure functions
8. **Handle All Cases**: Use Result types, never throw exceptions
9. **Lazy Evaluation**: Defer computation until needed
10. **Immutable Data**: Never mutate, always return new values

## Resources

- [Professor Frisby's Mostly Adequate Guide](https://mostly-adequate.gitbook.io/mostly-adequate-guide/)
- [Functional-Light JavaScript](https://github.com/getify/functional-light-js)
- [Fantasy Land Specification](https://github.com/fantasyland/fantasy-land)
- [JavaScript Allongé](https://leanpub.com/javascriptallongesix/read)
