// 下面是一个简单的 JavaScript 示例代码，演示如何在网页上点击按钮后弹出提示框。

document.addEventListener("DOMContentLoaded", function() {
    // 创建一个按钮元素
    const btn = document.createElement("button");
    btn.textContent = "点击我试试";
    document.body.appendChild(btn);

    // 给按钮添加点击事件
    btn.addEventListener("click", function() {
        alert("你点击了按钮！");
    });
});
