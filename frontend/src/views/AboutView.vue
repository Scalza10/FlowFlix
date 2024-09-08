<template>
  <div class="about-container">
    <div class="about-card">
      <h1>About Us</h1>
      <p>
        Welcome to my application! I am dedicated to providing the best service possible. As a passionate Software Engineer and Developer, I strive to continuously improve and innovate.
      </p>
      <div class="about-content">
        <div class="about-section">
          <h2>My Mission</h2>
          <p>
            My mission is to deliver high-quality products that bring value to users. I am committed to continuous improvement and innovation to meet the needs of my customers.
          </p>
        </div>
        <div class="about-section">
          <h2>About Me</h2>
          <ul>
            <li>Sebastian Calzadilla - Software Engineer and Developer</li>
          </ul>
        </div>
        <div class="about-section">
          <h2>Contact Me</h2>
          <p>
            If you have any questions or feedback, feel free to reach out to me at <a href="mailto:info@ourapp.com">info@ourapp.com</a>.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutView",
};
</script>

<style scoped>
.about-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: linear-gradient(to right, #4e4eff, #920092);
  min-height: 100vh;
}

.about-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

.about-content {
  text-align: left;
}

.about-section {
  margin-bottom: 20px;
}

.about-section h2 {
  color: #42b983;
  margin-bottom: 10px;
}

.about-section p,
.about-section ul {
  color: #333;
}

.about-section ul {
  list-style-type: none;
  padding: 0;
}

.about-section ul li {
  margin-bottom: 5px;
}

.about-section a {
  color: #42b983;
  text-decoration: none;
}

.about-section a:hover {
  text-decoration: underline;
}
</style>