module moveLight(
    input clk,
    output reg[15:0] led,
    input wire btnR,
    input wire btnL
);
initial
led[15] = 1;
reg controlR = 0;
reg controlL = 0;
always @(posedge clk) begin
    controlR <= btnR;
    controlL <= btnL;
        if(controlR == 0 & btnR == 1 & !led[0]) begin
            led <= led >> 1;
        end
        if(controlL == 0 & btnL == 1 & !led[15]) begin
            led <= led << 1;
        end
end
endmodule
    
