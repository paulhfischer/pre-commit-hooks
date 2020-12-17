# pre-commit-hooks

Some style-checkers and -fixers for [pre-commit](https://github.com/pre-commit/pre-commit).

### Usage

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/paulhfischer/pre-commit-hooks
    rev: v1.0.0
    hooks:
        - id: ...
```

### Available hooks

#### `format-general`

Formats all files that are not touched by the other hooks of this repo with
[prettier](https://github.com/prettier/prettier/).

Recommended `.prettierrc`:

```json
{
    "printWidth": 100,
    "tabWidth": 4,
    "singleQuote": true,
    "trailingComma": "all"
}
```

#### `format-web`

Formats all HTML/PHP-files with [js-beautify](https://github.com/beautify-web/js-beautify/).

Recommended `.jsbeautifyrc`:

```json
{
    "wrap_line_length": 100,
    "wrap_attributes": "force-expand-multiline",
    "end_with_newline": true,
    "content_unformatted": ["pre", "style", "script"]
}
```

#### `lint-css`

Lints and attempts to fix all CSS/SCSS/SASS-files with
[stylelint](https://github.com/stylelint/stylelint/).

Recommended `.stylelintrc`:

```json
{
    "extends": "stylelint-config-airbnb",
    "rules": {
        "indentation": 4
    }
}
```

#### `lint-javascript`

Lints and attempts to fix all JS-files with [eslint](https://github.com/eslint/eslint).

Recommended `.eslintrc`:

```json
{
    "plugins": ["html", "jinja2"],
    "extends": ["airbnb-base", "prettier", "plugin:prettier/recommended"],
    "env": {
        "browser": true,
        "commonjs": true,
        "jquery": true,
        "es6": true
    },
    "rules": {
        "jsx-a11y/label-has-associated-control": "off",
        "import/no-cycle": "off"
    }
}
```

#### `lint-javascript-react`

Lints and attempts to fix all JS/JSX-files with [eslint](https://github.com/eslint/eslint).

Recommended `.eslintrc`:

```json
{
    "plugins": ["@typescript-eslint", "html", "jinja2"],
    "extends": [
        "airbnb-base",
        "airbnb/hooks",
        "prettier",
        "prettier/react",
        "plugin:prettier/recommended"
    ],
    "env": {
        "browser": true,
        "commonjs": true,
        "jest": true,
        "node": true,
        "es6": true
    },
    "rules": {
        "jsx-a11y/label-has-associated-control": "off",
        "import/no-cycle": "off"
    },
    "settings": {
        "react": {
            "version": ""  # enter your react version here
        }
    }
}
```

#### `lint-typescript`

Lints and attempts to fix all TS-files with [eslint](https://github.com/eslint/eslint).

Recommended `.eslintrc`:

```json
{
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "project": "./tsconfig.json",
        "createDefaultProgram": true
    },
    "plugins": ["@typescript-eslint", "html", "jinja2"],
    "extends": [
        "airbnb-typescript/base",
        "plugin:@typescript-eslint/recommended",
        "prettier",
        "prettier/@typescript-eslint",
        "plugin:prettier/recommended"
    ],
    "env": {
        "browser": true,
        "commonjs": true,
        "jest": true,
        "node": true,
        "es6": true
    },
    "rules": {
        "jsx-a11y/label-has-associated-control": "off",
        "import/no-cycle": "off"
    }
}
```

Recommended `tsconfig.json`:

```json
{
    "compilerOptions": {
        "target": "es5",
        "lib": ["dom", "dom.iterable", "esnext"],
        "allowJs": true,
        "skipLibCheck": true,
        "esModuleInterop": true,
        "allowSyntheticDefaultImports": true,
        "strict": true,
        "forceConsistentCasingInFileNames": false,
        "module": "esnext",
        "isolatedModules": true,
        "moduleResolution": "Node",
        "noEmit": false,
        "resolveJsonModule": true
    }
}
```

#### `lint-typescript-react`

Lints and attempts to fix all TS/TSX-files with [eslint](https://github.com/eslint/eslint).

Recommended `.eslintrc`:

```json
{
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "project": "./tsconfig.json",
        "createDefaultProgram": true
    },
    "plugins": ["@typescript-eslint", "html", "jinja2"],
    "extends": [
        "airbnb-typescript",
        "airbnb/hooks",
        "plugin:@typescript-eslint/recommended",
        "prettier",
        "prettier/react",
        "prettier/@typescript-eslint",
        "plugin:prettier/recommended"
    ],
    "env": {
        "browser": true,
        "commonjs": true,
        "jquery": true,
        "es6": true
    },
    "rules": {
        "jsx-a11y/label-has-associated-control": "off",
        "import/no-cycle": "off"
    },
    "settings": {
        "react": {
            "version": ""  # enter your react version here
        }
    }
}
```

Recommended `tsconfig.json`:

```json
{
    "compilerOptions": {
        "target": "es5",
        "lib": ["dom", "dom.iterable", "esnext"],
        "allowJs": true,
        "skipLibCheck": true,
        "esModuleInterop": true,
        "allowSyntheticDefaultImports": true,
        "strict": true,
        "forceConsistentCasingInFileNames": false,
        "module": "esnext",
        "isolatedModules": true,
        "moduleResolution": "Node",
        "noEmit": false,
        "jsx": "react",
        "resolveJsonModule": true
    }
}
```
