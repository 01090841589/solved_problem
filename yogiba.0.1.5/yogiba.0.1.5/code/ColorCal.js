module.exports.function = function colorCal(colorTestStart, colorInput) {
  const console = require('console');
  var blindnessSet = require('blindnessSet.js')
  var cnt = 0;
  var visited = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  var num = colorInput;
  if (colorTestStart != undefined) {
    if (colorTestStart.colorArray != undefined) {
      cnt = colorTestStart.colorArray.color_Stat;
      if (colorTestStart.colorArray.color_One != 0) {
        visited[1] = colorTestStart.colorArray.color_One;
        if (colorTestStart.colorArray.color_One == -1) {
          visited[1] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Two != 0) {
        visited[2] = colorTestStart.colorArray.color_Two;
        if (colorTestStart.colorArray.color_Two == -1) {
          visited[2] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Three != 0) {
        visited[3] = colorTestStart.colorArray.color_Three;
        if (colorTestStart.colorArray.color_Three == -1) {
          visited[3] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Four != 0) {
        visited[4] = colorTestStart.colorArray.color_Four;
        if (colorTestStart.colorArray.color_Four == -1) {
          visited[4] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Five != 0) {
        visited[5] = colorTestStart.colorArray.color_Five;
        if (colorTestStart.colorArray.color_Five == -1) {
          visited[5] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Six != 0) {
        visited[6] = colorTestStart.colorArray.color_Six;
        if (colorTestStart.colorArray.color_Six == -1) {
          visited[6] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Seven != 0) {
        visited[7] = colorTestStart.colorArray.color_Seven;
        if (colorTestStart.colorArray.color_Seven == -1) {
          visited[7] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Eight != 0) {
        visited[8] = colorTestStart.colorArray.color_Eight;
        if (colorTestStart.colorArray.color_Eight == -1) {
          visited[8] = colorInput;
        }
      }
      if (colorTestStart.colorArray.color_Nine != 0) {
        visited[9] = colorTestStart.colorArray.color_Nine;
        if (colorTestStart.colorArray.color_Nine == -1) {
          visited[9] = colorInput;
        }
      }
    }
  }
  // var itt = blindnessSet[0].normal;

  var acblind = 0;
  var acweak = 0;
  var normal = 0;
  var rgblind = 0;
  var rgweak = 0;
  var i = 0;
  var buf = 0;
  if (cnt == 9) {
    for (i = 1; i < 10; i++) {
      buf = 0;
      var items = blindnessSet[i-1];
      if (visited[i] == items.normal){
        normal += 1;
        buf += 1;
      }
      if (visited[i] == items.rg_color_blindness){
        rgblind += 1;
        buf += 1;
      }
      if (visited[i] == items.rg_color_weakness){
        rgweak += 1;
        buf += 1;
      }
      if (visited[i] == items.al_color_blindness){
        acblind += 1;
        buf += 1;
      }
      if (visited[i] == items.al_color_weakness){
        acweak += 1;
        buf += 1;
      }
      if (buf == 0){
          if( items.rg_color_blindness == 0){
            rgblind += 1;
          }
          if( items.rg_color_weakness == 0){
            rgweak += 1;
          }
          if( items.al_color_blindness == 0){
            acblind += 1;
          }
          if( items.al_color_weakness == 0){
            acweak += 1;
          }
      }
    }
  }

  console.log(normal);
  console.log(rgblind);
  console.log(rgweak);
  console.log(acblind);
  console.log(acweak);
  return {
    color_One: visited[1],
    color_Two: visited[2],
    color_Three: visited[3],
    color_Four: visited[4],
    color_Five: visited[5],
    color_Six: visited[6],
    color_Seven: visited[7],
    color_Eight: visited[8],
    color_Nine: visited[9],
    color_Stat: cnt,
    aCBlind: acblind,
    aCWeak: acweak,
    normals: normal,
    rGBlind: rgblind,
    rGWeak: rgweak,
  }
}
