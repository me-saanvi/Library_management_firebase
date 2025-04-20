const formContainer = document.getElementById("formContainer");
const output = document.getElementById("output");
const operations = {
  addBook: ["Book ID", "Title", "Author", "Published Year", "Genre"],
  deleteBook: ["Book ID"],
  displayBooks: [],
  searchBook: ["Title Keyword"],
  addUser: ["User ID", "Username", "Email"],
  deleteUser: ["User ID"],
  showUsers: [],
  searchUser: ["Field (username/email)", "Value"],
  updateUser: ["User ID", "Field", "New Value"],
  borrowBook: ["User ID", "Book ID", "Duration (days)"],
  returnBook: ["User ID", "Book ID"],
  showBorrowed: ["User ID"],
  updateBook: ["Book ID", "Field", "New Value"]
};

document.getElementById("operationSelect").addEventListener("change", function () {
  const selected = this.value;
  formContainer.innerHTML = "";

  if (!selected) return;

  const fields = operations[selected];
  const form = document.createElement("form");

  fields.forEach((labelText, i) => {
    const input = document.createElement("input");
    input.type = "text";
    input.placeholder = labelText;
    input.name = `field${i}`;
    form.appendChild(input);
    form.appendChild(document.createElement("br"));
  });

  const submit = document.createElement("button");
  submit.textContent = "Submit";
  submit.type = "submit";
  form.appendChild(submit);

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const values = Array.from(form.elements)
      .filter((el) => el.name && el.value)
      .map((el) => el.value);

    // Call the appropriate API (placeholder)
    try {
      const res = await fetch(`/api/${selected}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ values })
      });

      const data = await res.json();
      output.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
      output.textContent = "❌ Error connecting to backend: " + err;
    }
  });

  formContainer.appendChild(form);
});


    
  
  
  