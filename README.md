# 🛒 Agentic Retail SKU Demand Assistant

This project is an interactive **Agentic AI-based Retail Assistant** built using LangChain and Groq’s LLaMA3 model. It enables business users to query retail SKU-level sales, demand, pricing, inventory, and more — using both **RAG-based retrieval** and **analytical tools like trend plots**.

---

## 💡 Key Features

- ✅ Ask natural language questions about sales, inventory, pricing, demand, seasonality.
- 📊 Generate **SKU-level sales trend visualizations** dynamically.
- 🧠 Combines **LLM + Vector DB (FAISS)** to enable context-aware responses.
- 🔗 Agent-enabled via LangChain with custom tools.
- 🌐 Deployable via **Streamlit Cloud**.

---

## 📁 Project Structure

├── data/
│ └── retail_store_inventory.csv # Main dataset
├── src/
│ ├── agent_chain.py # Agent + tool integration
│ ├── csv_retriver.py # FAISS retriever loader
│ └── query_chain.py # (Optional) for non-agent RAG
├── tools/
│ └── plot_sales_tools.py # Trend plotting tool
├── ui/
│ └── app.py # Streamlit UI app
├── vectorstores_csv/ # FAISS vector DB
├── .env # Local API key holder
└── README.md


---

## 🚀 How It Works

1. **RAG (Retrieval-Augmented Generation)** is used to fetch relevant CSV data based on user queries.
2. **Agent Tools** handle structured tasks like plotting sales trends, extracting insights, etc.
3. A **LangChain agent** orchestrates tool usage + LLM responses.
4. Powered by **Groq's LLaMA3** for ultra-fast, context-aware answers.

---

## 🧪 Example Prompts

You can ask:

- **"What are the top 3 products with highest demand forecast this month?"**
- **"Plot the sales trend of Product ID P0005 in Region East over the last 3 months."**
- **"Which SKUs are overstocked in the South region?"**
- **"Suggest products suitable for discounting based on low sales and high inventory."**
- **"How is competitor pricing affecting Electronics category in Summer?"**

---

## 📦 Setup Locally

### 1. Clone Repo

```bash
git clone https://github.com/ubsingh9/retail-sku-demand.git
cd retail-sku-demand
```
### 2. Install Dependencies
pip install -r requirements.txt
```
```
### 3. 3. Set Environment Variable
Option A: Add .env file

GROQ_API_KEY=your_groq_api_key

Option B: On Streamlit Cloud, add in secrets manager:

GROQ_API_KEY = "your_groq_api_key"
```
```
### 4. Run Locally
streamlit run ui/app.py
```
```
### 📦 Deploy on Streamlit Cloud
1. Push your repo to GitHub.
2. Go to https://streamlit.io/cloud and connect GitHub.
3. Select this project to deploy.
4. Under Settings > Secrets, add:
GROQ_API_KEY = "your_groq_api_key"
5. Click Deploy.
```
```
### ⚙️ Tech Stack
Layer	Tool
🧠 LLM	Groq llama3-8b-8192
🔍 Vector DB	FAISS + LangChain
📈 Charts	Matplotlib
🧰 Agent Tools	LangChain Toolkits
🌐 UI	Streamlit
```
```
### 📜 Prompt Samples (for Markdown / testing)
1. What are the top 5 SKUs with the highest sales in the last 30 days?
2. Plot the sales trend of Product ID P0005 in Region East over the last 3 months.
3. Which SKUs have high inventory but low sales across all stores?
4. Suggest any discounts we can offer for Groceries in the North region.
5. What is the impact of competitor pricing on Electronics category during Summer?
```
```
### 🚧 Future Enhancements
Add Time Series Forecasting (LSTM/Prophet) for demand prediction.
Include Dynamic Pricing Suggestions.
Integrate SKU Alerts for out-of-stock/overstock situations.
Add multi-page Streamlit UI with charts, tables, and scenario analysis.
```
```
# 👤 Author
Uday Singh
📧 [icfai.uday@gmail.com]
🔗 [https://www.linkedin.com/in/udaysingh3/]
```
```
### 📄 License
Licensed under the MIT License – see the LICENSE file for details.
```