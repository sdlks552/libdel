### 语法

   background-color
    设置背景颜色
    `background-color:#FFFFFF` 设置div颜色为白色

   border
    设置边框
    `border: 1px solid black` 
    边框设置为1像素，solid(实线)样式，黑色

   background
    `background:url(./path/xxx.png) no-repeat 10px 10px`
    将 `./path/xxx.png` 设置为背景图片，如果图片尺寸小于div大小，会直接将图片放置多个填满div
    使用no-repeat可以使它不自动平铺，图片过大可以让其默认平铺
    10px 10px表示在div的坐标x,y显示图片，以div左上角为原点，第一个x可以使用right与left表示水平左右对齐，第二个可以用top与bottom表示上下对齐，也可以使用center让它居中对齐
    要让背景图片与背景颜色共存可以让颜色写在图片后面

  background-size
    设置背景图片的纵横比
    cover值可以保持图片原本的纵横比，将图片覆盖到整个div，而这个可能会导致比例不一的图片某些部分看不到
    `background:cover`
    contain这个值会保持图片的纵横比，并使图片适应整个div，但也有些区域不会被覆盖，即保留一些区域
    `background:contain`