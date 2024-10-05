module bnfled(
input clk,
output reg [15:0] led
);
initial
led[15] = 1;
reg [32:0] counter;   
reg oldcounter; 
always @ (posedge clk) begin
oldcounter <= counter[25];
if (counter[25] != oldcounter) begin
    if(led[15] & !led[0])begin
        led[15] <= 0;
        led[0] <= 1;
    end else
            if(led[0] & !led[15]) begin
                led[0] <= 0;
                led[15] <= 1;
            end
    end else
            counter <= counter + 1;
end
endmodule
