const mongoose = require("mongoose");

const StudentSchema = new mongoose.Schema({
  Student_Name: String,
  age: Number,
  Phone_no: String,
  Subject: String
});

module.exports = mongoose.model("Student", StudentSchema);
