function convertTo24Hour(
  hour: number,
  minutes: number,
  period: string,
) {
  let convertedHour = hour;

  if (period.toUpperCase() === "AM") {
    if (hour === 12) {
      convertedHour = 0;
    }
  } else if (period.toUpperCase() === "PM") {
    if (hour !== 12) {
      convertedHour = hour + 12;
    }
  }

  return {
    hour: convertedHour,
    minutes,
  };
}

console.log(convertTo24Hour(3, 0, "PM"));
console.log(convertTo24Hour(11, 30, "PM"));
console.log(convertTo24Hour(12, 0, "AM"));
console.log(convertTo24Hour(7, 45, "AM"));

