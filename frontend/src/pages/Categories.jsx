import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Search, Filter, Grid, List, ChevronRight } from 'lucide-react';

const Categories = () => {
  const [viewMode, setViewMode] = useState('grid');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');

  // Mock categories data
  const categories = [
    {
      id: 1,
      name: 'Electronics',
      description: 'Latest gadgets and electronic devices',
      image: 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=400&h=300&fit=crop',
      productCount: 156,
      subcategories: ['Smartphones', 'Laptops', 'Headphones', 'Cameras', 'Smart Home']
    },
    {
      id: 2,
      name: 'Clothing',
      description: 'Fashion and apparel for all occasions',
      image: 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400&h=300&fit=crop',
      productCount: 234,
      subcategories: ['Men\'s Clothing', 'Women\'s Clothing', 'Kids\' Clothing', 'Shoes', 'Accessories']
    },
    {
      id: 3,
      name: 'Home & Kitchen',
      description: 'Everything for your home and kitchen needs',
      image: 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400&h=300&fit=crop',
      productCount: 189,
      subcategories: ['Furniture', 'Kitchen Appliances', 'Home Decor', 'Bedding', 'Storage']
    },
    {
      id: 4,
      name: 'Books',
      description: 'Wide selection of books and educational materials',
      image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=300&fit=crop',
      productCount: 89,
      subcategories: ['Fiction', 'Non-Fiction', 'Educational', 'Children\'s Books', 'E-books']
    },
    {
      id: 5,
      name: 'Sports & Outdoors',
      description: 'Gear for sports and outdoor activities',
      image: 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop',
      productCount: 145,
      subcategories: ['Fitness Equipment', 'Outdoor Gear', 'Sports Apparel', 'Team Sports', 'Water Sports']
    },
    {
      id: 6,
      name: 'Health & Beauty',
      description: 'Personal care and beauty products',
      image: 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400&h=300&fit=crop',
      productCount: 167,
      subcategories: ['Skincare', 'Makeup', 'Hair Care', 'Health Supplements', 'Personal Care']
    },
    {
      id: 7,
      name: 'Toys & Games',
      description: 'Fun toys and games for all ages',
      image: 'https://images.unsplash.com/photo-1558060370-d644479cb6f7?w=400&h=300&fit=crop',
      productCount: 98,
      subcategories: ['Action Figures', 'Board Games', 'Educational Toys', 'Outdoor Toys', 'Video Games']
    },
    {
      id: 8,
      name: 'Automotive',
      description: 'Car accessories and automotive parts',
      image: 'https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400&h=300&fit=crop',
      productCount: 76,
      subcategories: ['Car Parts', 'Accessories', 'Tools', 'Car Care', 'Electronics']
    }
  ];

  const filteredCategories = categories.filter(category =>
    category.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    category.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const CategoryCard = ({ category }) => (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div className="relative">
        <img
          src={category.image}
          alt={category.name}
          className="w-full h-48 object-cover"
        />
        <div className="absolute top-4 right-4 bg-primary-600 text-white px-2 py-1 rounded-full text-sm font-medium">
          {category.productCount} items
        </div>
      </div>
      
      <div className="p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-2">{category.name}</h3>
        <p className="text-gray-600 mb-4">{category.description}</p>
        
        <div className="mb-4">
          <h4 className="text-sm font-medium text-gray-700 mb-2">Popular Subcategories:</h4>
          <div className="flex flex-wrap gap-2">
            {category.subcategories.slice(0, 3).map((sub, index) => (
              <span
                key={index}
                className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full"
              >
                {sub}
              </span>
            ))}
            {category.subcategories.length > 3 && (
              <span className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full">
                +{category.subcategories.length - 3} more
              </span>
            )}
          </div>
        </div>
        
        <Link
          to={`/products?category=${encodeURIComponent(category.name.toLowerCase())}`}
          className="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium"
        >
          Browse Products
          <ChevronRight className="w-4 h-4 ml-1" />
        </Link>
      </div>
    </div>
  );

  const CategoryListItem = ({ category }) => (
    <div className="bg-white rounded-lg shadow-md p-6 flex items-center space-x-6 hover:shadow-lg transition-shadow duration-300">
      <img
        src={category.image}
        alt={category.name}
        className="w-24 h-24 object-cover rounded-lg"
      />
      
      <div className="flex-1">
        <div className="flex items-center justify-between mb-2">
          <h3 className="text-xl font-semibold text-gray-900">{category.name}</h3>
          <span className="bg-primary-100 text-primary-600 px-3 py-1 rounded-full text-sm font-medium">
            {category.productCount} items
          </span>
        </div>
        
        <p className="text-gray-600 mb-3">{category.description}</p>
        
        <div className="flex items-center justify-between">
          <div className="flex flex-wrap gap-2">
            {category.subcategories.slice(0, 4).map((sub, index) => (
              <span
                key={index}
                className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full"
              >
                {sub}
              </span>
            ))}
          </div>
          
          <Link
            to={`/products?category=${encodeURIComponent(category.name.toLowerCase())}`}
            className="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium"
          >
            Browse Products
            <ChevronRight className="w-4 h-4 ml-1" />
          </Link>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Shop by Categories</h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Discover our wide range of product categories and find exactly what you're looking for
          </p>
        </div>

        {/* Search and Filters */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <div className="flex flex-col md:flex-row gap-4 items-center justify-between">
            {/* Search */}
            <div className="flex-1 max-w-md">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="text"
                  placeholder="Search categories..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                />
              </div>
            </div>

            {/* View Mode Toggle */}
            <div className="flex items-center space-x-2">
              <span className="text-sm text-gray-600">View:</span>
              <div className="flex bg-gray-100 rounded-lg p-1">
                <button
                  onClick={() => setViewMode('grid')}
                  className={`p-2 rounded-md transition-colors ${
                    viewMode === 'grid'
                      ? 'bg-white text-primary-600 shadow-sm'
                      : 'text-gray-600 hover:text-gray-900'
                  }`}
                >
                  <Grid className="w-4 h-4" />
                </button>
                <button
                  onClick={() => setViewMode('list')}
                  className={`p-2 rounded-md transition-colors ${
                    viewMode === 'list'
                      ? 'bg-white text-primary-600 shadow-sm'
                      : 'text-gray-600 hover:text-gray-900'
                  }`}
                >
                  <List className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Categories Count */}
        <div className="mb-6">
          <p className="text-gray-600">
            Showing {filteredCategories.length} of {categories.length} categories
          </p>
        </div>

        {/* Categories Grid/List */}
        {viewMode === 'grid' ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {filteredCategories.map(category => (
              <CategoryCard key={category.id} category={category} />
            ))}
          </div>
        ) : (
          <div className="space-y-6">
            {filteredCategories.map(category => (
              <CategoryListItem key={category.id} category={category} />
            ))}
          </div>
        )}

        {/* No Results */}
        {filteredCategories.length === 0 && (
          <div className="text-center py-12">
            <div className="text-gray-400 mb-4">
              <Search className="w-16 h-16 mx-auto" />
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">No categories found</h3>
            <p className="text-gray-600">
              Try adjusting your search terms or browse all categories
            </p>
            <button
              onClick={() => setSearchTerm('')}
              className="mt-4 px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
            >
              Show All Categories
            </button>
          </div>
        )}

        {/* Featured Categories Section */}
        <div className="mt-16">
          <h2 className="text-2xl font-bold text-gray-900 mb-8 text-center">Featured Categories</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {categories.slice(0, 3).map(category => (
              <div key={category.id} className="relative group">
                <div className="relative overflow-hidden rounded-lg">
                  <img
                    src={category.image}
                    alt={category.name}
                    className="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                  <div className="absolute inset-0 bg-black bg-opacity-40 group-hover:bg-opacity-50 transition-all duration-300"></div>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <div className="text-center text-white">
                      <h3 className="text-2xl font-bold mb-2">{category.name}</h3>
                      <p className="text-sm opacity-90 mb-4">{category.productCount} Products</p>
                      <Link
                        to={`/products?category=${encodeURIComponent(category.name.toLowerCase())}`}
                        className="inline-block bg-white text-gray-900 px-6 py-2 rounded-lg font-medium hover:bg-gray-100 transition-colors"
                      >
                        Shop Now
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Categories;