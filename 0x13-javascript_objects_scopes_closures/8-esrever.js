exports.esrever = function (list) {
  const l = list.length;
  const new_array = [];
  for (let i = l - 1; i >= 0; i--) {
    new_array.push(list[i]);
  }
  return new_array;
};
