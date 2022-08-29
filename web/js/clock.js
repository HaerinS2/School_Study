function tick(){
  var month, date, hours, minutes, seconds, ap;
  var intYear, intDate, intMon,intHours,intMinutes,intSeconds;
  var today;
  today = new Date();
  intYear = today.getFullYear();
  intMon = today.getMonth()+1;
  intDate = today.getDate();
  intHours = today.getHours();
  intMinutes = today.getMinutes();
  intSeconds = today.getSeconds();
  if (intMon < 10){
      month = "0"+intMon;
  }
  else{
      month = intMon;
  }

  if (intDate < 10){
      date = '0'+intDate;
  }
  else{
      date = intDate;
  }

  if (intHours == 0){
      hours = '12:';
      ap = 'AM';
  }
  else if (intHours < 12){
      hours = intHours+':';
      ap = 'AM';
  }
  else if (intHours == 12){
      hours = '12:';
      ap = 'PM';
  }
  else{
      intHours = intHours-12;
      hours = intHours + ':';
      ap = 'PM';
  }

  if(intMinutes < 10){
      minutes = '0'+intMinutes;
  }
  else{
      minutes = intMinutes+':';
  }

  if (intSeconds < 10){
      seconds = '0'+ intSeconds;
  }
  else{
      seconds = intSeconds;
  }

  timeString = intYear + '-' + month + '-' + date + ' ' + hours + minutes + seconds + ' ' + ap;
  Clock.innerHTML = timeString;
  window.setTimeout('tick();',100);
}
window.onload = tick;