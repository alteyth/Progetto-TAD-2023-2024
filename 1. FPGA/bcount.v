module bcount(
input clk,
output reg [15:0] led
);
reg [32:0] counter;   
reg oldcounter;

always @ (posedge clk) begin
oldcounter <= counter[25];
    if (counter[25] != oldcounter) begin
        led <= led + 1;
        end else
                counter <= counter + 1;
end

 
endmodule
