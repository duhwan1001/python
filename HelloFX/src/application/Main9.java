package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main9 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();

			TextField tfNum = (TextField) scene.lookup("#tfNum");
			Button b1 = (Button) scene.lookup("#b1");
			Button b2 = (Button) scene.lookup("#b2");
			Button b3 = (Button) scene.lookup("#b3");
			Button b4 = (Button) scene.lookup("#b4");
			Button b5 = (Button) scene.lookup("#b5");
			Button b6 = (Button) scene.lookup("#b6");
			Button b7 = (Button) scene.lookup("#b7");
			Button b8 = (Button) scene.lookup("#b8");
			Button b9 = (Button) scene.lookup("#b9");
			Button b0 = (Button) scene.lookup("#b0");
			Button btnCall = (Button) scene.lookup("#btnCall");
			
			b1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("1");
					System.out.println(tfNum.getLength());
				}
			});
			b2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("2");
					System.out.println(tfNum.getLength());
				}
			});
			b3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("3");
					System.out.println(tfNum.getLength());
				}
			});
			b3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("3");
					System.out.println(tfNum.getLength());
				}
			});
			b4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("4");
					System.out.println(tfNum.getLength());
				}
			});
			b5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("5");
					System.out.println(tfNum.getLength());
				}
			});
			b6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("6");
					System.out.println(tfNum.getLength());
				}
			});
			b7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("7");
					System.out.println(tfNum.getLength());
				}
			});
			b8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("8");
					System.out.println(tfNum.getLength());
				}
			});
			b9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("9");
					System.out.println(tfNum.getLength());
				}
			});
			b0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.appendText("0");
					if(tfNum.getLength() == 3) {
						tfNum.appendText("-");
					}
					System.out.println(tfNum.getLength());
				}
			});
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					tfNum.clear();
					System.out.println(tfNum.getLength());
				}
			});
			
			if(tfNum.getLength() == 3) {
				tfNum.appendText("-");
			}
			if(tfNum.getLength() == 7) {
				tfNum.appendText("-");
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		launch(args);
	}
}
