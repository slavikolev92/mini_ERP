document.addEventListener("DOMContentLoaded", function() {
  const orderIdInput = document.getElementById("orderId");
  const detailsCard = document.getElementById("orderDetails");

  orderIdInput.addEventListener("input", async function() {
    const orderId = orderIdInput.value.trim();
    if (orderId === "") {
      detailsCard.classList.add("d-none");
      return;
    }

    try {
      const response = await fetch(`/order/${orderId}`);
      if (!response.ok) throw new Error("Order not found");
      const data = await response.json();

      document.getElementById("customerName").textContent = data.customer_name;
      document.getElementById("orderDate").textContent = data.order_date;
      document.getElementById("quantity").textContent = data.quantity;
      document.getElementById("status").textContent = data.status;

      detailsCard.classList.remove("d-none");
    } catch (err) {
      detailsCard.classList.add("d-none");
    }
  });
});
