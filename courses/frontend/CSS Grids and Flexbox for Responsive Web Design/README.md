# CSS Grids and Flexbox for Responsive Web Design

[Course Resources](https://github.com/jen4web/fem-layout.git)

- Float
- Flexbox(basically usages in `image` gallery system)
- Flexbox usages as grid layout.

## Table of Contents

- [CSS Grids and Flexbox for Responsive Web Design](#css-grids-and-flexbox-for-responsive-web-design)
  - [Table of Contents](#table-of-contents)
    - [Introduction to Setup](#introduction-to-setup)
      - [Resources](#resources)
      - [Defining Responsive Design](#defining-responsive-design)
    - [Floats](#floats)
      - [Overview of Floats](#overview-of-floats)
      - [Float Exercise](#float-exercise)
    - [Flexbox](#flexbox)
      - [Introducing Flexbox](#introducing-flexbox)
      - [Flex Snippets/ Properties](#flex-snippets-properties)

### Introduction to Setup

#### Resources

[Course Resources](https://github.com/jen4web/fem-layout.git)

#### Defining Responsive Design

Defined by three characteristics

- **Flexible grid-based layout**
  ![images](images/1.png)
- **Media Queries(CSS3)**
  ![images](images/2.png)
- **Images that resizes**
  ![images](images/3.png)

**Picture Tag**:

`<picture>` tag is brand new HTML 5.1 tag that most commonly used for **responsive** design.

```html
<picture>
  <!-- if screen size at least 650px, logo-big.jpg is showing -->
  <source media="(min-width: 650px)" srcset="logo-big.jpg" />
  <!-- if screen size at least 465px, logo-medium.jpg is showing -->
  <source media="(min-width: 465px)" srcset="logo-medium.jpg" />
  <!-- if screen size at less then 465px, logo-small.jpg is showing -->
  <img src="logo-small.jpg" />
</picture>
```

### Floats

- `float` is a CSS a property, we can assume that without `float` property we cannot make an webpage or website.

- `float` has `two` values.

![images](images/4.png)

```css
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

body {
  font-family: tahoma;
}

div {
  /* outline: 1px solid red; */
  float: left;
  height: 300px;
}

.ione .itwo .ithree {
  width: 24.5%;
}

.text-one,
.text-two,
.text-three {
  padding-left: 10px;
  width: 74.5%;
}

.text-three {
  float: right;
}
```

```html
<body>
  <div class="ione">
    <img src="./images/1-200x300.jpg" alt="" />
  </div>
  <div class="text-one">
    <h1>Computer</h1>
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Adipisci
      voluptate nemo tenetur hic, quaerat, obcaecati placeat, suscipit similique
      nam eius omnis quisquam velit blanditiis consectetur. Minima earum aliquid
      officiis quas.
    </p>
    <br />
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod incidunt
      earum quo consequuntur, voluptatibus voluptas officiis tempore voluptates
      quasi vero?
    </p>
    <p>lorem500</p>
  </div>
  <div class="text-two">
    <h1>Computer</h1>
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Adipisci
      voluptate nemo tenetur hic, quaerat, obcaecati placeat, suscipit similique
      nam eius omnis quisquam velit blanditiis consectetur. Minima earum aliquid
      officiis quas.
    </p>
    <br />
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod incidunt
      earum quo consequuntur, voluptatibus voluptas officiis tempore voluptates
      quasi vero?
    </p>
    <p>lorem500</p>
  </div>
  <div class="itwo">
    <img src="./images/2-200x300.jpg" alt="" />
  </div>
  <div class="text-three">
    <h1>Computer</h1>
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Adipisci
      voluptate nemo tenetur hic, quaerat, obcaecati placeat, suscipit similique
      nam eius omnis quisquam velit blanditiis consectetur. Minima earum aliquid
      officiis quas.
    </p>
    <br />
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod incidunt
      earum quo consequuntur, voluptatibus voluptas officiis tempore voluptates
      quasi vero?
    </p>
    <p>lorem500</p>
  </div>

  <div>
    <img src="./images/3-200x300.jpg" alt="" />
  </div>
</body>
```

![images](images/5.png)

#### Overview of Floats

```text
float: left/right;
clear: left/right/both;
```

![images](images/6.png)

```css
* {
  box-sizing: border-box;
}

.row::after {
  content: "";
  clear: both;
  display: table;
}

.col-1 {
  float: left;
  margin-left: 4%;
  width: 21%;
  background-color: darkblue;
  height: 130px;
  margin-bottom: 2pc;
}

.text-center {
  text-align: center;
  padding: 45px 0;
  font-weight: bold;
  font-size: 30px;
  color: white;
}

@media only screen and (min-width: 480px) and (max-width: 767px) {
  .col-1 {
    width: 44%;
  }
}

@media only screen and (max-width: 479px) {
  .col-1 {
    width: 98%;
  }
}

/* attribute selector 
 * Any column that starts with col- is selected. 
*/
/* [class*="col-"] {
    background-color: red;
} */

.col-pull {
  left: -74%;
}
```

```html
<body>
  <div class="row">
    <div class="text-center col-1">col-1</div>
    <div class="text-center col-1">col-2</div>
    <div class="text-center col-1">col-3</div>
    <div class="text-center col-1 col-pull">col-4</div>
  </div>
</body>
```

| Large Screen             | Medium Screen           | Small Screen            |
| ------------------------ | ----------------------- | ----------------------- |
| ![images](images/10.png) | ![images](images/8.png) | ![images](images/9.png) |

#### Float Exercise

![images](images/border-box.png)

### Flexbox

#### Introducing Flexbox

![images](images/11.png)

![images](images/12.png)

#### Flex Snippets/ Properties

```css
ul {
  display: -webkit-flex; /* target chrome, Safari */
  display: -ms-flexbox; /* target IE10 */
  display: flex;
}
```

**flex-direction**: `row(default)`, `row-reverse`, `column`, `column-reverse`

| Where    | Snippets                          | Output                   |
| -------- | --------------------------------- | ------------------------ |
|          | `Initial`                         | ![images](images/13.png) |
| `parent` | `display: flex;`                  | ![images](images/14.png) |
| `parent` | `flex-direction: column;`         | ![images](images/15.png) |
| `parent` | `flex-direction: column-reverse;` | ![images](images/16.png) |
| `parent` | `flex-direction: row-reverse;`    | ![images](images/17.png) |

**flex-wrap**: `wrap`, `wrap-reverse`, `nowrap(default)`

| Where    | Snippets                   | Output                   |
| -------- | -------------------------- | ------------------------ |
| `parent` | `flex-wrap: wrap;`         | ![images](images/18.png) |
| `parent` | `flex-wrap: nowrap;`       | ![images](images/19.png) |
| `parent` | `flex-wrap: wrap-reverse;` | ![images](images/20.png) |

**flex-flow**:

> **flex-flow**: `flex-direction` `flex-wrap`.
> **flex-flow** is the **shorthand** for both `flex-direction` and `flex-wrap`

| Where    | Snippets                       | Output                   |
| -------- | ------------------------------ | ------------------------ |
| `parent` | `flex-flow: row wrap-reverse;` | ![images](images/21.png) |
