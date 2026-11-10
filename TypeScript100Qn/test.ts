function getTomorrowDate() {
  const tomorrrow = new Date();
  tomorrrow.setDate(tomorrrow.getDate() + 1)
  return tomorrrow;
}
console.log(getTomorrowDate());