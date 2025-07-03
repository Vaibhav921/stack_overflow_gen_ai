# Stack Overflow Clone (Angular Frontend)

This is an Angular-based frontend for a Stack Overflow clone.

## Prerequisites

- [Node.js](https://nodejs.org/) (v16 or later recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- Backend API running at `http://localhost:5000/answers` (update the URL in [`src/app/answer.service.ts`](src/app/answer.service.ts) if different)

## Setup

1. **Install dependencies:**
   ```sh
   npm install
   ```

2. **Start the development server:**
   ```sh
   npm start
   ```
   This will run `ng serve` and start the app at [http://localhost:4200](http://localhost:4200).

3. **Usage:**
   - Open your browser and go to [http://localhost:4200](http://localhost:4200).
   - Enter a question and click "Search" to fetch answers.
   - Use the "Sort with AI" checkbox to toggle AI-based sorting.

## Build

To build the project for production:

```sh
npm run build
```

The output will be in the `dist/stack-clone` directory.

## Notes

- Make sure your backend server is running and accessible at the URL specified in [`src/app/answer.service.ts`](src/app/answer.service.ts).
- You can customize styles in [`src/styles.css`](src/styles.css).

---
```# filepath: README.md

# Stack Overflow Clone (Angular Frontend)

This is an Angular-based frontend for a Stack Overflow clone.

## Prerequisites

- [Node.js](https://nodejs.org/) (v16 or later recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- Backend API running at `http://localhost:5000/answers` (update the URL in [`src/app/answer.service.ts`](src/app/answer.service.ts) if different)

## Setup

1. **Install dependencies:**
   ```sh
   npm install
   ```

2. **Start the development server:**
   ```sh
   npm start
   ```
   This will run `ng serve` and start the app at [http://localhost:4200](http://localhost:4200).

3. **Usage:**
   - Open your browser and go to [http://localhost:4200](http://localhost:4200).
   - Enter a question and click "Search" to fetch answers.
   - Use the "Sort with AI" checkbox to toggle AI-based sorting.

## Build

To build the project for production:

```sh
npm run build
```

The output will be in the `dist/stack-clone` directory.

## Notes

- Make sure your backend server is running and accessible at the URL specified in [`src/app/answer.service.ts`](src/app/answer.service.ts).
- You can customize styles in [`src/styles.css`](src/styles.css)