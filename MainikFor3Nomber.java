package komer.nol.project;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.annotation.SuppressLint;
import android.graphics.Color;
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
        final ConstraintLayout backgroundes = (ConstraintLayout)findViewById(R.id.backgroundes);

        kitty.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View view) {
                says++;
                one.setText("I said nyaaaaa " + says +" times");
                if (says % 2 == 0){
                    backgroundes.setBackgroundColor(Color.RED);
                }
                else{
                    backgroundes.setBackgroundColor(Color.rgb(255,0,255));
                }
            }
        });
    }
}