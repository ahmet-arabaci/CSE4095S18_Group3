package com.main;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Iterator;

import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFCreationHelper;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class DBConnection {

	public static void main(String[] args) throws FileNotFoundException, IOException, ParseException, ClassNotFoundException, SQLException {
	    
		/*
		for(int i=0; i<63; i++){
			//insertToDB("export(" + i + ").json", "Bekar" , i+1);
		}*/
		/*
		for(int i=67; i<104; i++){
			insertToDB("export("+ (i-63) + ").json", "Cocuklu", i+1);
		}*/
		getExcel();
	}

	public static void insertToDB(String filename,String classlabel, int i) throws FileNotFoundException, IOException, ParseException, ClassNotFoundException, SQLException{
		
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/datascience_db","root","etr123");  
		Statement stmt= con.createStatement();  
	
		JSONParser parser = new JSONParser();
		JSONArray Tweetler = (JSONArray)parser.parse(new FileReader("/home/oguz/Dev/workspaces/datascience_projectup/Data_Science/src/com/datascience/" + classlabel + "/" + filename));

		  for (Object Tweet : Tweetler)
		  {
		    JSONObject data = (JSONObject) Tweet;

		    String tweet = (String) data.get("Tweet");
		    System.out.println(tweet);
		    String label = (String) data.get("Label");
		    System.out.println(label);
		 
		    if(label.equals("BEKAR")){
		    	if( !(tweet.contains("\\")) ){
		    		tweet = tweet.replaceAll("\"", "");
		    		if( tweet.length() <= 500 ){
		    			stmt.executeUpdate("INSERT INTO Document (doc_id, text,class_id) VALUES (" + i + ",\"" + tweet + "\", 1)");
			    	} 
		    	}
		    }
		    else if(label.equals("COCUKLU")){
		    	if( !(tweet.contains("\\")) ){
		    		tweet = tweet.replaceAll("\"", "");
		    		if( tweet.length() <= 500 ){
		    			stmt.executeUpdate("INSERT INTO Document (doc_id, text,class_id) VALUES (" + i + ",\"" + tweet + "\", 3)"); 
		    		}
		    	}
		    }
		    
		  }
		  con.close();
	}
	
	public static void getExcel() throws ClassNotFoundException, SQLException, IOException{
		XSSFWorkbook wb = new XSSFWorkbook();
		XSSFCreationHelper createHelper = wb.getCreationHelper();
		XSSFSheet sheet = wb.createSheet("Data Science Report");
  
		int rowNum = 0;
        XSSFRow row = sheet.createRow(rowNum++);
        XSSFCell cell = row.createCell(0);
        cell.setCellValue("id");
        cell = row.createCell(1);
        cell.setCellValue("doc_id");
        cell = row.createCell(2);
        cell.setCellValue("text");
        
        // --------------------------------------------------------------
        Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/datascience_db","root","etr123");
		Statement stmt = con.createStatement();
		String sql = "SELECT id,doc_id,text FROM Document";
		ResultSet rs = stmt.executeQuery(sql);
		while(rs.next()){
			int colNum = 0;
			row = sheet.createRow(rowNum++);
			String isRead = rs.getString("id");
			cell = row.createCell(colNum++);
            cell.setCellValue(isRead);
			String isDisplay = rs.getString("doc_id");
			cell = row.createCell(colNum++);
            cell.setCellValue(isDisplay);
			String isDownload = rs.getString("text");
			cell = row.createCell(colNum++);
            cell.setCellValue(isDownload);
		}
		FileOutputStream out = new FileOutputStream(new File("/home/oguz/Desktop/java_demo.xlsx"));
		wb.write(out);
        out.close();
        wb.close();
        rs.close();
		con.close();
		
		System.out.println("Excel Printed.");
  }
}
