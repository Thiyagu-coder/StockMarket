import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Trading App",
    page_icon=":heavy_dollar_sign:",
    layout="wide",
)

# Put your HTML page as a string (triple quotes)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trading Guide App</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        /* Your CSS here (I kept your code as is) */
        :root {
            --primary-color: #007bff;
            --secondary-color: #28a745;
            --background-color: #f8f9fa;
            --card-background: #ffffff;
            --text-color: #343a40;
            --light-text-color: #6c757d;
            --border-color: #e9ecef;
            --shadow: rgba(0, 0, 0, 0.08);
            --header-bg: linear-gradient(to right, #007bff, #0056b3);
        }
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; } header { background: var(--header-bg); color: white; padding: 40px 0; text-align: center; box-shadow: 0 4px 10px var(--shadow); border-bottom-left-radius: 15px; border-bottom-right-radius: 15px; } header h1 { font-family: 'Montserrat', sans-serif; font-size: 3.5em; margin-bottom: 10px; letter-spacing: 1.5px; } header h2 { font-family: 'Montserrat', sans-serif; font-size: 1.8em; font-weight: 400; opacity: 0.9; margin-top: 0; } .hero-section { display: flex; align-items: center; justify-content: center; padding: 50px 0; background-color: var(--card-background); margin-top: 30px; border-radius: 15px; box-shadow: 0 4px 12px var(--shadow); flex-wrap: wrap; /* Allow wrapping on smaller screens */ } .hero-content { flex: 1; padding-right: 40px; min-width: 300px; /* Ensure content doesn't get too small */ } .hero-content h3 { font-family: 'Montserrat', sans-serif; font-size: 2.2em; color: var(--primary-color); margin-bottom: 15px; } .hero-content p { font-size: 1.1em; color: var(--light-text-color); margin-bottom: 25px; } .hero-image { flex: 1; text-align: center; min-width: 300px; /* Ensure image doesn't get too small */ } .hero-image img { max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 6px 20px var(--shadow); } .services-section { padding: 60px 0; text-align: center; } .services-section h2 { font-family: 'Montserrat', sans-serif; font-size: 2.8em; color: var(--text-color); margin-bottom: 40px; position: relative; display: inline-block; } .services-section h2::after { content: ''; position: absolute; width: 80px; height: 4px; background-color: var(--primary-color); left: 50%; transform: translateX(-50%); bottom: -10px; border-radius: 2px; } .service-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 40px; } .service-card { background-color: var(--card-background); padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px var(--shadow); text-align: left; transition: transform 0.3s ease, box-shadow 0.3s ease; border-left: 5px solid var(--primary-color); } .service-card:hover { transform: translateY(-8px); box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12); } .service-card h4 { font-family: 'Montserrat', sans-serif; font-size: 1.5em; color: var(--primary-color); margin-top: 0; margin-bottom: 15px; display: flex; align-items: center; } .service-card h4 .icon { font-size: 1.2em; margin-right: 10px; color: var(--secondary-color); } .service-card p { font-size: 1em; color: var(--light-text-color); } /* Responsive Adjustments */ @media (max-width: 768px) { header h1 { font-size: 2.5em; } header h2 { font-size: 1.4em; } .hero-section { flex-direction: column; text-align: center; } .hero-content { padding-right: 0; margin-bottom: 30px; } .services-section h2 { font-size: 2em; } .service-card { padding: 25px; } } @media (max-width: 480px) { header h1 { font-size: 2em; } header h2 { font-size: 1.2em; } .hero-content h3 { font-size: 1.8em; } .service-cards { grid-template-columns: 1fr; } } /* Icons for services - using pseudo-elements for more control */ .service-card.one h4::before { content: '1️⃣'; margin-right: 10px; font-size: 1.2em; } .service-card.two h4::before { content: '2️⃣'; margin-right: 10px; font-size: 1.2em; } .service-card.three h4::before { content: '3️⃣'; margin-right: 10px; font-size: 1.2em; } .service-card.four h4::before { content: '4️⃣'; margin-right: 10px; font-size: 1.2em; }
        
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Trading Guide App 📈</h1>
            <h2>Your Smart Companion for Informed Investments</h2>
        </div>
    </header>
    <main class="container">
        <section class="hero-section">
            <div class="hero-content">
                <h3>Unlock Your Investment Potential</h3>
                <p>We provide the greatest platform for you to collect all information prior to investing in stocks. Our comprehensive tools and insights empower you to make smarter decisions in the dynamic world of trading.</p>
            </div>
            <div class="hero-image">
                <img src="https://via.placeholder.com/600x400/007bff/ffffff?text=Trading+App+Screenshot" alt="Trading App Interface">
            </div>
        </section>
        <section class="services-section">
            <h2>Our Comprehensive Services</h2>
            <div class="service-cards">
                <div class="service-card one">
                    <h4>Stock Information</h4>
                    <p>See real-time stock data, historical performance, and profiles.</p>
                </div>
                <div class="service-card two">
                    <h4>Stock Prediction</h4>
                    <p>Forecast closing prices for the next 30 days based on models.</p>
                </div>
                <div class="service-card three">
                    <h4>CAPM Return</h4>
                    <p>Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stocks asset based on its risk and market performance

.</p>
                </div>
                <div class="service-card four">
                    <h4>CAPM Beta</h4>
                    <p>Calculates Beta and Expected Return for Individual Stocks..</p>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
"""

# Display full HTML inside Streamlit
components.html(html_code, height=1200, scrolling=True)
