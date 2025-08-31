export default function getStudentsByLocation(array, city) {
  if (!Array.isArray(array)) return [];
  return array.filter(student => student.location === city);
}
