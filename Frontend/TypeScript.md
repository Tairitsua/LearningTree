# TypeScript

`JavaScript` 是 `dynamic type`，而 `TypeScript` 把它变成了 `static type`，即需要声明类型了。

似乎导包需要 `@type/express` 和 `express` 的 `js` 包都得要。前者纯粹定义 `type`，后者才是具体实现？

然后全都换成了 `import` 写法。

> `nvm`/`npm`/`Node` 与 `Express` 相关笔记已移至 [Node 与 npm](Node与npm.md)（2026-09-30 治理拆分）。

## 接口

```typescript
interface LabelledValue {
  label: string;
}
```

只需要一个 `obj` 含有 `label`：`{label:xxx}`，就说这个对象实现了这个接口，可以传入。

## 问题

`Element` 类型找不到，是需要在 `tsconfig.json` 中 `compilerOptions` 中的 `"lib": ["es6","dom"]` 添加 `dom`。

[TypeScript error: Element implicitly has an 'any' type because expression of type 'string' can't be used to index type](https://github.com/DefinitelyTyped/DefinitelyTyped/issues/52383)

try to import a `CommonJS` module into an `ES6` module （如 `import path from 'path'`）需要在 `"compilerOptions"` 中添加 `"esModuleInterop": true`

[TypeScript: Module can only be default-imported using the 'esModuleInterop' flag](https://bobbyhadz.com/blog/typescript-module-can-only-be-default-imported-esmoduleinterop)
