import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#To print all the columns of the file
pd.set_option('display.max_columns',None)

#Query: To show how many restaurants provide online or not
def offline_orders(main):
    m=main.drop(columns=['restaurant type','table booking','cuisines type','area','Unnamed','Unnamed: 0'],axis=1)
    n=pd.get_dummies(m['online_order'])
    a=pd.concat([m,n],axis=1)
    b=a.drop(columns=['online_order'],axis=1)
    offline_orders=[b['No'].sum(),b['Yes'].sum()]
    labels=['Online orders','Offline orders']
    colors=['Lightcoral','Lightgreen']
    plt.figure(figsize=(6,6))
    explode=(0,0)
    plt.pie(offline_orders, labels=labels, autopct='%1.0f%%', startangle=90, colors=colors, explode=explode)
    plt.title("Orders of restaurant offline or not")
    plt.show()

#Query: To show what price range is preffered by couples/two people at restaurant
def analyze_price_range(df):

    #Makes bins of the price range
    df['price_range'] = pd.cut(df['avg cost (two people)'],bins=[0, 300, 600, 1000, 2000, 6000],
                               labels=['₹0-300', '₹301-600', '₹601-1000', '₹1001-2000', '₹2000+'])
    df['weighted_score'] = df['rate (out of 5)'] * df['num of ratings']

    
    analysis = df.groupby('price_range').agg({
        'weighted_score': 'sum',
        'num of ratings': 'sum'
    }).reset_index()

    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(analysis['price_range'], analysis['weighted_score'], color='lightblue')

    #Loop to write at the top of the bars
    for bar in bars:
        x = bars.index(bar)
        total_ratings = analysis['num of ratings'].iloc[x]
        avg_rating = (analysis['weighted_score'].iloc[x] / total_ratings).round(2)
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f'Score: {int(bar.get_height()):,}\nRatings: {int(total_ratings):,}\nAvg: {avg_rating}/5',
                 ha='center', va='bottom')

    plt.title('Price Range Preference Analysis\n(Based on Rating × Number of Ratings)', pad=20)
    plt.xlabel('Price Range for Two People')
    plt.ylabel('Weighted Score (Rating × Number of Ratings)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

#Query: To show which types of restaurats are most favoured by the public
def analyze_favorite_cuisines(df):

    # For missing values
    df['cuisines type'] = df['cuisines type'].fillna('Others')

    # Split if contain 2 names
    cuisine_data = df.assign(cuisines_type=df['cuisines type'].str.split(',')).explode('cuisines_type')

    # Clean names
    cuisine_data['cuisines_type'] = cuisine_data['cuisines_type'].str.strip()

    # Group by cuisine and calculate total ratings
    cuisine_analysis = cuisine_data.groupby('cuisines_type')['num of ratings'].agg('sum').reset_index()

    top_cuisines = cuisine_analysis.nlargest(15, 'num of ratings')

    plt.figure(figsize=(12, 6))

    # Create bars and color with seabon's function(color_palate)
    bars = plt.bar(top_cuisines['cuisines_type'],
                   top_cuisines['num of ratings'],
                   color=sns.color_palette("husl", 15))

    plt.title('Most Favored Restaurant Types Based on Number of Ratings',
              pad=20, fontsize=14)
    plt.xlabel('Cuisine Type', fontsize=12)
    plt.ylabel('Total Number of Ratings', fontsize=12)

    # Loop to write on top of the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f'{int(height):,}',
                 ha='center', va='bottom')

    plt.xticks(rotation=45, ha='right')

    plt.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()


    plt.show()

# Exeption that reads data and clean it
try:
    
    df = pd.read_csv(r"C:\Users\DELL\Downloads\zomato.csv")
 
    df = df.dropna(subset=['avg cost (two people)', 'rate (out of 5)', 'num of ratings'])
    for col in ['avg cost (two people)', 'rate (out of 5)', 'num of ratings']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df[df['avg cost (two people)'].between(0, 6000) &
            df['rate (out of 5)'].between(0, 5) &
            df['num of ratings'] > 0]
    offline_orders(df)
    analyze_favorite_cuisines(df)
    analyze_price_range(df)


except Exception as e:
    print(f"An error occurred: {str(e)}")






