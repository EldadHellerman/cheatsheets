//4 bit wide 8 by 16 multidimensional array:
bit [3:0] multidimensional_array [0:7] [1:16];
//bit is 1 or 0. logic can also be z (high impedance) or x (unknowen - used for simulation).

//modules are the main building blocks.
//modules have inputs and outputs.
//module can have parameters passed in when initialized to controll their properties.

module mux1(
    output logic out,
    input logic a, b, sel
);
    //'and', 'or', 'not' are primitives. there are many more.
    //#2 is simulation propegation time
    and #2 g1(f1, a, n_sel),
           g1(f2, b, sel);
    or #2 g3(out, f1, f2);
    not g4(n_sel, sel);
endmodule: mux //tag to signify end of what

//equivelant module:
module mux2( output logic out, input logic a, b, sel);
    assign out = (a & ~sel) | (b & sel);
endmodule

//equivelant module:
module mux3( output logic out, input logic a, b, sel);
    always_comb out = (a & ~sel) | (b & sel);
endmodule

//simulation module:
module muxSim;
    logic [3:0] count;
    logic a, b, sel, out;
    //instantiating a module
    mux1 mux_first (.*); //all local names match all module names
    mux2 mux_second (.*); //all local names match all module names
    mux3 mux_third (.*); //all local names match all module names
    initial begin
        //monitor will execute every time one of it's inputs change state
        //it will print at the end of current simulatino time
        $monitor($time, " a=%b, b=%b, sel=%b, out=%b",a,b,sel,out)
        //$display will print once the currnet values (before end of current simulation time)
        for(i=4'b0; i<4'b1000; i++) begin
            //{} are used to concatenate bits together.
            //[] re used for bit range select. even in reverse order.
            {sel,b,a} = i[0:2];
            #10; //delay of 10
        end
        //$finish is used to finish simulation.
        #10 $finish;
    end
endmodule;


    parameter  = ;
    enum data_type {  } name;
    typedef enum data_type {  } name;
    //logic types will be inferred as wire or reg, depending on their use.

    //always_ff used for 
    always_ff @( clock ) begin : blockName
        
    end
    //always_comb used for combinatinoal logic:
    always_comb begin : blockName
        
    end

    unique case (param)
        : 
        default: 
    endcase
    mod_name instance_name (.*);
endmodule