
  function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
    while (0 !== currentIndex) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
    return array;
  }
  
  function check(var1){
    bool = false
    for (var i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]) {
      if (var1 == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"][i]) {
        bool = true
      }
    }
    return bool 
  }
  
  function mate(gen1, gen2) {
    possibilities = [gen1[0]+gen2[0], gen1[0]+gen2[1], gen1[1]+gen2[0], gen1[1]+gen2[1]];
    possibilities = shuffle(possibilities);
    litter = [possibilities[0],possibilities[1]];
    if (check(litter[0][1])){
      litter[0] = [litter[0][1]+litter[0][0]];
    }
    if (check(litter[1][1])){
      litter[1] = [litter[1][1]+litter[1][0]];
    } return litter
  }
  
  function mate1(gen1, gen2) {
    litter1 = mate(gen1[0]+gen1[1], gen2[0]+gen2[1])
    litter2 = mate(gen1[2]+gen1[3], gen2[2]+gen2[3])
    litter = [litter1[0]+litter2[0], litter1[1]+litter2[1]]
    return litter
  }
  
  for (var i = 0; i < 5; i++) {
    document.write(mate("ss", "ss")+"<br>")
    document.write(mate1("GgLl","GgLl")+"<br>")
  }