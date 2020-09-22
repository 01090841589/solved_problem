module.exports.function = function start_mode (modeinfo) {
  var result = 0;
  var color = modeinfo.color;
  if (modeinfo.mode.color == true){
    result = '색맹';
  }
  else if (modeinfo.mode.sight == true){
    result = '시력';
    
  }
  else if (modeinfo.mode.farsight == true){
    result = '난시';
  }
  else{
    result = '오류';
  }
  return result;
}


