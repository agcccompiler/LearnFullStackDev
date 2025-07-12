// 下面是一个较长但不难的 JavaScript 代码示例，实现了一个简单的猜数字游戏，并包含了一些基础的数组、字符串、循环、条件、函数等用法，适合初学者理解。

// 猜数字游戏
function guessNumberGame() {
    // 生成 1 到 100 之间的随机整数
    const answer = Math.floor(Math.random() * 100) + 1;
    let guessCount = 0;
    let guessedNumbers = [];
    let maxTries = 10;
    let success = false;

    alert("欢迎来到猜数字游戏！\n我已经想好了 1 到 100 之间的一个数字。\n你有 10 次机会来猜。");

    while (guessCount < maxTries) {
        let input = prompt(`请输入你猜的数字（第 ${guessCount + 1} 次，共 ${maxTries} 次）：`);
        if (input === null) {
            alert("你已取消游戏。");
            break;
        }
        let guess = Number(input);

        if (isNaN(guess) || guess < 1 || guess > 100) {
            alert("请输入 1 到 100 之间的有效数字！");
            continue;
        }

        guessCount++;
        guessedNumbers.push(guess);

        if (guess === answer) {
            alert(`恭喜你，猜对了！答案就是 ${answer}。\n你一共猜了 ${guessCount} 次。\n你的所有猜测：${guessedNumbers.join(", ")}`);
            success = true;
            break;
        } else if (guess < answer) {
            alert("你猜的数字太小了！");
        } else {
            alert("你猜的数字太大了！");
        }
    }

    if (!success && guessCount === maxTries) {
        alert(`很遗憾，机会用完了。正确答案是 ${answer}。\n你的所有猜测：${guessedNumbers.join(", ")}`);
    }
}

// 统计一段文字中每个字母出现的次数（不区分大小写，只统计英文字母）
function countLetters(text) {
    let counts = {};
    for (let i = 0; i < text.length; i++) {
        let ch = text[i].toLowerCase();
        if (ch >= 'a' && ch <= 'z') {
            if (counts[ch]) {
                counts[ch]++;
            } else {
                counts[ch] = 1;
            }
        }
    }
    return counts;
}

// 打印字母统计结果
function printLetterCounts(text) {
    let result = countLetters(text);
    let output = "字母统计结果：\n";
    for (let key in result) {
        output += `${key}: ${result[key]}\n`;
    }
    alert(output);
}

// 生成斐波那契数列前 n 项
function fibonacci(n) {
    if (n <= 0) return [];
    if (n === 1) return [0];
    let arr = [0, 1];
    for (let i = 2; i < n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    return arr;
}

// 打印斐波那契数列
function showFibonacci() {
    let n = prompt("请输入要生成的斐波那契数列项数（正整数，最大 30）：");
    n = Number(n);
    if (isNaN(n) || n <= 0 || n > 30) {
        alert("输入无效！");
        return;
    }
    let arr = fibonacci(n);
    alert(`前 ${n} 项斐波那契数列：\n${arr.join(", ")}`);
}

// 主菜单
function mainMenu() {
    while (true) {
        let choice = prompt(
            "请选择功能：\n" +
            "1. 猜数字游戏\n" +
            "2. 字母统计\n" +
            "3. 斐波那契数列\n" +
            "4. 退出"
        );
        if (choice === null) {
            alert("已退出。");
            break;
        }
        switch (choice.trim()) {
            case "1":
                guessNumberGame();
                break;
            case "2":
                let text = prompt("请输入要统计的英文文本：");
                if (text !== null) {
                    printLetterCounts(text);
                }
                break;
            case "3":
                showFibonacci();
                break;
            case "4":
                alert("感谢使用，再见！");
                return;
            default:
                alert("无效选择，请重新输入。");
        }
    }
}

// 启动主菜单
mainMenu();
