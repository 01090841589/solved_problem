module.exports.function = function visionTest(modeName, colorArray) {// 예) (3, 4, plus(더하기))
  const console = require('console');
  var result = 0;
  var name = '';
  var cnt = 0;
  var visited = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  if (colorArray != undefined) {
    cnt = colorArray.color_Stat;
    cnt += 1;
    if (colorArray.color_One > 0) {
      visited[1] = colorArray.color_One;
    }
    if (colorArray.color_Two > 0) {
      visited[2] = colorArray.color_Two;
    }
    if (colorArray.color_Three > 0) {
      visited[3] = colorArray.color_Three;
    }
    if (colorArray.color_Four > 0) {
      visited[4] = colorArray.color_Four;
    }
    if (colorArray.color_Five > 0) {
      visited[5] = colorArray.color_Five;
    }
    if (colorArray.color_Six > 0) {
      visited[6] = colorArray.color_Six;
    }
    if (colorArray.color_Seven > 0) {
      visited[7] = colorArray.color_Seven;
    }
    if (colorArray.color_Eight > 0) {
      visited[8] = colorArray.color_Eight;
    }
    if (colorArray.color_Nine > 0) {
      visited[9] = colorArray.color_Nine;
    }

  }
  modeName = String(modeName);

  if (modeName == "색맹") {
    name = "색맹";
    if (cnt <= 9) {
      result = Math.floor(Math.random() * 9) + 1;
      if (visited[result] != 0) {
        while (visited[result] != 0) {
          result = Math.floor(Math.random() * 9) + 1;
        }
      }
    }
    visited[result] = -1;
  }
  else {
    result = 10;
  }
  console.log(modeName);
  if (modeName == "시력") {
    name = "시력";
  }
  else if (modeName == "난시") {
    name = "난시";
  }







  return {
    modeName: name,
    colorOutput: result,
    colorArray: {
      color_One: visited[1],
      color_Two: visited[2],
      color_Three: visited[3],
      color_Four: visited[4],
      color_Five: visited[5],
      color_Six: visited[6],
      color_Seven: visited[7],
      color_Eight: visited[8],
      color_Nine: visited[9],
      color_Ten: visited[10],
      color_Stat: cnt,
    }
  }
}
