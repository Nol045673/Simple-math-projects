package komer.nol.project;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    int says = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final TextView one = (TextView)findViewById(R.id.morecat);
        ImageButton kitty = (ImageButton)findViewById(R.id.imageButton4);

        kitty.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View view) {
                says++;
                one.setText("I said nyaaaaa " + says +" times");
            }
        });

    }
}