module buttonCled(
    input clk,
    output reg[7:0] led,
    input wire btnC
);
reg [7:0] debounce;
reg state = 0;
reg control = 1;
always @(posedge clk) begin
    led[0] <= state;

    if(btnC) begin
        if(debounce < 8'd10) begin
            debounce <= debounce + 1;
        end
    end else begin
        debounce <= 0;
    end

    if(debounce == 8'd10)
        if(control) begin
            state <= state + 1;
            control <= control + 1;
        end
    else begin
        if(!control)
            control <= control + 1;
        end

end
endmodule