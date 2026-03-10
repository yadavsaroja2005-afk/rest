const express = require("express");
const mongoose = require("mongoose");
const Student = require("./models/student");

const app = express();
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/studentdb")
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.log(err));

app.post("/students", async (req, res) => {
  const student = new Student(req.body);
  const result = await student.save();
  res.send(result);
});

app.get("/students", async (req, res) => {
  const students = await Student.find();
  res.send(students);
});

app.get("/students/:id", async (req, res) => {
  const student = await Student.findById(req.params.id);
  res.send(student);
});

app.put("/students/:id", async (req, res) => {
  const updatedStudent = await Student.findByIdAndUpdate(
    req.params.id,
    req.body,
    { new: true }
  );
  res.send(updatedStudent);
});

app.delete("/students/:id", async (req, res) => {
  await Student.findByIdAndDelete(req.params.id);
  res.send({ message: "Student deleted" });
});

app.listen(3000, () => {
  console.log("Server running on port 3000 For REST SERVICES");
});
